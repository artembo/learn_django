from django import forms
from django.forms import NumberInput

from firstapp.models import Contact, Person


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.all()

    person = forms.ModelChoiceField(label='', queryset=Person.objects.none(), widget=NumberInput(attrs={'hidden': True}))

    class Meta:
        fields = '__all__'
        model = Contact
