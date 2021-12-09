from django.forms import ModelForm, EmailInput

from persons.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'mail': EmailInput(attrs={'type': 'email'})
        }








