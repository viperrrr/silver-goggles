from multiprocessing import AuthenticationError
from statistics import mode
from typing import Text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)
