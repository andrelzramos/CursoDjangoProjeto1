from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #http response
    return render(request, 'home.html')

