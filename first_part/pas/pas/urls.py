"""pas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from persons.views import personDetails, newPerson, editPerson
from webapp.views import welcome, goodbye, contact, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome), # describe the function name in views.
    path('goodbye.html', goodbye),
    path('contact', contact),
    path('home', home, name='index'),
    path('person_details/<int:id>', personDetails),
    path('new_person', newPerson),
    path('edit_person/<int:id>', editPerson)
]
