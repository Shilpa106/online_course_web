from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

# **********************homepage**********************

def home(request):
    return HttpResponse("Home Page")

# ***************end homepage**************************


