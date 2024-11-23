from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_question, name='add_question'),
    path('search/', views.search_question, name='search_question'),
]
