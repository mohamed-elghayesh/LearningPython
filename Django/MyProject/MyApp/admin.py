from django.contrib import admin
from .models import Publication, Article, Reporter

# Register your models here.
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Reporter)