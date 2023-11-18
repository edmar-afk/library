from django.db import models

# Create your models here.


class Respondents(models.Model):
    course = models.CharField(max_length=100)
    year_level = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)