import django
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('its my ome page')
def gm_view(request):
    return HttpResponse('good morning')

def ga_view(request):
    return HttpResponse('good afternoon')

def gn_view(request):
    return HttpResponse('good night')