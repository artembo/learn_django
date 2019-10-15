from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView

from firstapp.forms import ContactForm
from firstapp.models import Person, Contact


def index(request):
    people = Person.objects.prefetch_related('contacts')
    context = {
        'people': people
    }
    return render(request, 'firstapp.html', context)


class PersonView(DetailView, CreateView):
    model = Person
    queryset = Person.objects.prefetch_related('contacts')
    context_object_name = 'person'
    template_name = 'person.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_created')

    def get_initial(self):
        return {
            'person': self.kwargs.get('pk')
        }

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        print(form_kwargs)
        return form_kwargs


class ContactCreatedView(TemplateView):
    template_name = 'contact_successfully_added.html'
