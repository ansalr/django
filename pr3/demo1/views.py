from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one (request):
    return HttpResponse('one ')

def two (request):
    return HttpResponse('two')

def three (request):
    return HttpResponse('three')
