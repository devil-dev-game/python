from django.urls import path
from . import views

urlpatterns = [
    path('', views.audiobook_list, name='audiobook_list'),
]
