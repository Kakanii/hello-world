from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def good_hello(request):
    return HttpResponse("<h2>Hello Django! Good Morning !!</h1>")


def Night(request):
    date=datetime.datetime.now()
    s="<h4>Current date and time is :</h4>" + str(date)
    return HttpResponse(s)
