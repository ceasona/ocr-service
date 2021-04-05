from django.db import models


# Create your models here.

class Task(models.Model):
    input = models.TextField(null=True)
    output = models.TextField(null=True)
