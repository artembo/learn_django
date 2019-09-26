from django.shortcuts import render

from firstapp.models import Person


def index(request):
    people = Person.objects.all()
    context = {
        'people': people
    }
    return render(request, 'firstapp.html', context)
