from django.shortcuts import render
from django.http import HttpResponse
import datetime 
# Create your views here.



def display(request):
    return HttpResponse("<h1>display my first app</h1>")

def time(request):
    time = datetime.datetime.now()
    t = "<b>current time </b>"+str(time) 
    return HttpResponse(t)
