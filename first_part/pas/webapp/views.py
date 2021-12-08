from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Creation of welcome page
from persons.models import Person


def welcome(request): # request is necessary! It containts the user info of his request.

    messages = {'msg1': 'Message Value 1',
                'msg2': 'Another message'}


    # The return is necesarry! if not, the page will never be updated
    return render(request, 'welcome.html', messages)


def goodbye(request):
    return HttpResponse('Goodbye from Django!')


def contact(request):
    title = ' Contact Info '.center(50, '*')
    number = '\n Tel. Number: 555-555-51234'
    mail = '\n Mail: nonexistent@mail.com'
    response = title + number + mail
    return HttpResponse(response)

def home(request):
    number_persons = Person.objects.count()
    persons = Person.objects.all()
    return render(request, 'home.html', {'number_persons': number_persons, 'persons': persons})

