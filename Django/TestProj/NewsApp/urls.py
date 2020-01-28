from django.urls import path
from .views import NewsStatic, Home, Contact, NewsData, Register, AddUser, ModelForm, AddModelForm

urlpatterns = [
    path('', Home, name="home"),
    path('news-data/', NewsData, name="news-data"), # bacause of the default argument (year) in the views.NewsData()
    path('news-data/<int:year>/', NewsData, name="news-data"), # bacause of the default argument (year) in the views.NewsData()
    path('news/', NewsStatic, name="news"),
    path('contact-us/', Contact, name="contact-us"),
    path('sign-up/', Register, name="register"),
    path('add-user/', AddUser, name="add-user"),
    path('model-form/', ModelForm, name="model-form"),
    path('add-model-form/', AddModelForm, name="add-model-form"),
]
