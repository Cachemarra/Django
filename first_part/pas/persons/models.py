from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'Address {self.id}: {self.street}, {self.street_number}, {self.country}'

class Person(models.Model):
    # Static attributes.
    name = models.CharField(max_length=255) # Datatype CharField.
    last_name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Person {self.id}: {self.name} {self.last_name} {self.mail}'