from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, ListView

from firstapp.forms import ContactForm
from firstapp.models import Person


def index(request):
    people = Person.objects.all()
    context = {
        'people': people
    }
    return render(request, 'firstapp.html', context)


class IndexView(ListView):
    queryset = Person.objects.prefetch_related('contacts')
    template_name = 'firstapp.html'
    context_object_name = 'people'


def person_view(request, pk):
    person = Person.objects.get(pk=pk)

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.person = person
            contact.save()
            return render(request, 'contact_successfully_added.html')

    form = ContactForm(initial={'person': person})
    context = {
        'person': person,
        'form': form
    }
    return render(request, 'person.html', context)


class PersonContactCreateView(DetailView, CreateView):
    model = Person
    context_object_name = 'person'
    template_name = 'person.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_created')

    def get_initial(self):
        return {'person': self.object}


class ContactCreatedView(TemplateView):
    template_name = 'contact_successfully_added.html'
