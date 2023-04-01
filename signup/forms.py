from home.models import Video
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from login.models import coders
from home.models import Video

class codersform(ModelForm):
    class Meta:
        model = coders
        exclude = ['name','pasw']

class codersform2(ModelForm):
    class Meta:
            model = coders
            fields= '__all__'

class videoform(ModelForm):
    class Meta:
        model = Video
        exclude = ['ps']
        






