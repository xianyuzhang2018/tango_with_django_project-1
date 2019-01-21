from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>about</a>")

def about(request):
    return HttpResponse("Rango says this is about!  <br/> <a href='/rango/'>index</a>")