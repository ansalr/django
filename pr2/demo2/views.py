from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def time(request):
    ps_time = datetime.datetime.now()
    return HttpResponse('time is ; '+str(ps_time))