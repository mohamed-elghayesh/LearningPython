from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# from django.template import loader

# Create your views here.
""" def index(request):
    # return HttpResponse("Hello World !!")
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list':latest_question_list}
    # return HttpResponse(template.render(context, request))
    
    return render(request, 'polls/index.html', context) """

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    # returns the last 5 questions
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
    # returns the last 5 questions not including those with pub_date in the future
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

""" def detail(request, question_id):
    #return HttpResponse("You are looking at question %s" %question_id)
    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question doesn't exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question}) """

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

""" def results(request, question_id):
    # return HttpResponse("You are looking at the results of question %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question}) """

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # return HttpResponse("You are voting on question %s" %question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice."})
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # always redirect to avoid posting twice incase a user pressed backspace
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))