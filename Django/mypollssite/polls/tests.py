from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime
from polls.models import Question

# Create your tests here.

# a method is related to a class, while a function just do what it is intended to do
def create_question(question_text, days):
    """ creates a question given question_text and an int representing days (+ve: future, -ve: past) """
    time = timezone.now() + datetime.timedelta(days=days)
    Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """if no questions exist, display a message"""
        response = self.client.get(reverse("polls:index"))
        self.assertEquals(response.status_code,200)
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_past_question(self):
        """questions with past pub_date are displayed in index.html"""
        create_question("Past question.",-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_future_question(self):
        """questions with future pub_date are not to be displayed in index, a message is displayed"""
        create_question("Future question.", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_future_question_and_past_question(self):
        """only past questions is to be displayed"""
        create_question("Past question.", -30)
        create_question("Future question.", 30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_two_past_questions(self):
        """index page can display multiple questions"""
        create_question("Past question 1.", -30)
        create_question("Past question 2.", -5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2.>', '<Question: Past question 1.>'])

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently() should return False for future pub_date
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_questions(self):
        """
        was_published_recently() should return False for older than 1 day pub_date
        """
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_questions(self):
        """
        was_published_recently() should return True for less than one day pub_date
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
