from django.urls import path

from . import views

urlpatterns = [
    path('word', views.get_word, name='get_word'),
]
