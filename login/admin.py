from django.contrib import admin
from django.db import models
from .models import coders

class codersModel(admin.ModelAdmin):
    list_display=['name','matid','semester']


admin.site.register(coders,codersModel)
# Register your models here.
