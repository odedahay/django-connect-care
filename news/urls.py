from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='news'),
    path('<slug:c_slug>/', views.news_detail, name='news_detail'),
]