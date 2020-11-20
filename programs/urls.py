from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='programs'),
    path('<slug:c_slug>/', views.program_detail, name='program_detail'),
]