from django.urls import path

from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('thank-you', views.thank_you, name='thank_you'),
]