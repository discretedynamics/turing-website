from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello in the public website")

def algorithms(request):
    return HttpResponse("Hello in the algorithms page")

def workflows(request):
    return HttpResponse("Hello in the workflows page")

def author(request):
    return HttpResponse("Hello in the authors page")