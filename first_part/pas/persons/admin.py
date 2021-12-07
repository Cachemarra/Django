from django.contrib import admin

# Register your models here.
from persons.models import Person, Address

admin.site.register(Person)
admin.site.register(Address)
