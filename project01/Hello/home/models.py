from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
class Excel(models.Model):
    

    Title=models.CharField(("Title"),max_length=255)
    authors=models.CharField(("authors"),max_length=255)
    dbid=models.CharField(("id"),max_length=255)