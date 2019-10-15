from django.urls import path

from firstapp.views import index, PersonView, ContactCreatedView

urlpatterns = [
    path('', index),
    path('person/<pk>/', PersonView.as_view()),
    path('person/contact/created/', ContactCreatedView.as_view(), name='contact_created')
]
