from django.core.exceptions import DisallowedHost
from django.db import models
from django.db.models.base import Model

class coders(models.Model):
    name = models.CharField(max_length=255)
    matid = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    Cf = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pasw = models.CharField(max_length=255)