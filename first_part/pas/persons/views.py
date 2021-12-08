from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404

# Create your views here.
from persons.models import Person


def personDetails(request, id):
    # person = Person.objects.get(pk=id) # pk  = primary key
    person = get_object_or_404(Person, pk=id)
    return render(request, 'persons/details.html', {'person': person})


PersonForm = modelform_factory(Person, exclude=[]) # Creation of a formulary with Person class

def newPerson(request):
    personForm = PersonForm()
    return  render(request, 'persons/new.html', {'personForm': personForm})

