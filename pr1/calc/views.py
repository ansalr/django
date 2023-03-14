from email import message
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wish (request):
    message = '<h1>hello Ansal haan</h>''<h2>hru?</h2>'
    return HttpResponse(message)
def login(request):
    message = '<h1>enter your name </h1>'
    return HttpResponse(message)
def home(request):
    return HttpResponse('hello world')