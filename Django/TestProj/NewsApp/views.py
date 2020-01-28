from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.contrib import messages
from .models import News, RegistrationData
from .forms import RegistationForm, RegistrationModelForm

# Create your views here.

def Home(request, year=""):
    context = {"name":"Karma Mohamed", "age":5}
    return render(request, "home.html", context) # context sends data to home.html
    # return HttpResponse("<h1>This is the Home Page in the NewsApp</h1>")

def NewsStatic(request, year=""):
    context = {"news_list":["first article","second article","third article"]}
    return render(request, "news.html", context=context)
    # return HttpResponse("<h1>This is the News Page in the NewsApp</h1>")

def Contact(request, year=""):
    context = {"my_num":1500}
    return render(request, "contact-us.html", context=context)
    # return HttpResponse("<h1>This is the Contact us Page in the NewsApp</h1>")

def NewsData(request, year=timezone.now().year):
    # obj = News.objects.all() # gets all rows
    obj = News.objects.filter(pub_date__year = year)
    context = {"year":year, "data":obj}
    return render(request, "news-data.html", context)

def Register(request):
    context = {"form":RegistationForm}
    return render(request, "sign-up.html", context)

def AddUser(request):
    form = RegistationForm(request.POST)
    if(form.is_valid()):
        my_register = RegistrationData(username=form.cleaned_data["username"],
                                       password=form.cleaned_data["password"],
                                       email=form.cleaned_data["email"],
                                       phone=form.cleaned_data["phone"])
        my_register.save()
        messages.add_message(request,messages.SUCCESS, "You have signed-up successfully")
    return redirect("register")

def ModelForm(request):
    context = {"modelform":RegistrationModelForm}
    return render(request, "model-form.html", context)

def AddModelForm(request):
    mymodelform = RegistrationModelForm(request.POST)
    if(mymodelform.is_valid()):
        mymodelform.save()
    return redirect("model-form")
