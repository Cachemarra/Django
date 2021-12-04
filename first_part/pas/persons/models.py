from django.db import models

# Create your models here.

class Person(models.Model):
    # Static attributes.
    name = models.CharField(max_length=255) # Datatype CharField.
    last_name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)

