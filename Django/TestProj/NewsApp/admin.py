from django.contrib import admin
from .models import News, SportsNews, RegistrationData

# Register your models here.
admin.site.register(News)
admin.site.register(SportsNews)
admin.site.register(RegistrationData)