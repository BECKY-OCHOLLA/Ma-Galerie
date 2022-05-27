from django.db import models

# Create your models here.
class location(models.model):
    name=models.CharField(max_length=50)
