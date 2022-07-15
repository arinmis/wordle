from django.urls import  path
from . import views

urlpatterns = [
    path("word/<int:length>/<int:amount>", views.get_word, name="get_word"), 

]
