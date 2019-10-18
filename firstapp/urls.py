from django.urls import path

from firstapp.views import index, person_view, ContactCreatedView, PersonContactCreateView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('person/<pk>/', person_view, name='person'),
    path('person/<pk>/', PersonContactCreateView.as_view(), name='person'),
    path('person/contact/created/', ContactCreatedView.as_view(), name='contact_created'),
]
