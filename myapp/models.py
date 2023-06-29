from django.db import models

# Create your models here.
class TestSistemSolar(models.Model): 
    ask = models.CharField(max_length=200)
    answer = models.CharField(max_length=50)



