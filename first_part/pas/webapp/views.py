from django.http import HttpResponse


# Create your views here.

# Creation of welcome page
def welcome(request): # request is necessary! It containts the user info of his request.
    # The return is necesarry! if not, the page will never be updated
    return HttpResponse('Hello World from Django!')


def goodbye(request):
    return HttpResponse('Goodbye from Django!')


def contact(request):
    title = ' Contact Info '.center(50, '*')
    number = '\n Tel. Number: 555-555-51234'
    mail = '\n Mail: nonexistent@mail.com'
    response = title + number + mail
    return HttpResponse(response)

