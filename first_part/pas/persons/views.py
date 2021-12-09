from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from persons.forms import PersonForm
from persons.models import Person


def personDetails(request, id):
    # person = Person.objects.get(pk=id) # pk  = primary key
    person = get_object_or_404(Person, pk=id)
    return render(request, 'persons/details.html', {'person': person})


# PersonForm = modelform_factory(Person, exclude=[]) # Creation of a formulary with Person class

def newPerson(request):

    if request.method == 'POST':
        personForm = PersonForm(request.POST)

        # Check if is valid
        if personForm.is_valid():
            personForm.save()
            # If is valid, we redirect to home page
            return redirect('index')
    else:
        personForm = PersonForm()

    return render(request, 'persons/new.html', {'personForm': personForm})


#%% Edit person
def editPerson(request, id):

    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        personForm = PersonForm(request.POST, instance=person)

        # Check if is valid
        if personForm.is_valid():
            personForm.save()
            # If is valid, we redirect to home page
            return redirect('index')
    else:
        personForm = PersonForm(instance=person)

    return render(request, 'persons/edit.html', {'personForm': personForm})
