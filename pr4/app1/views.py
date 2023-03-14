from email import message
from django.shortcuts import render


# Create your views here.

def display(request):
    return render (request,'app2_temp/ansal.html')