from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Day(request):
    return HttpResponse("<h1>Good day to you !!</h1>")
