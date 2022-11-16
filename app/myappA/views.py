from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.


# class PersonListView(ListView):
#     model = models.Person

def index(request):
    print(request)
    print(request)
