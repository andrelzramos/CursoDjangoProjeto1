from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #http response
    return render(request, 'home.html')

def my_view(request):
    #http response
    
    return HttpResponse('ISSO IRÁ APARECER NO CORPO DO HTML, Página Sobre')
