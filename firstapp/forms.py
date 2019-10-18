from django import forms

from firstapp.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ('service', 'link')

        fields = ('service', 'link', 'person')
        widgets = {'person': forms.HiddenInput()}
