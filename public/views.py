from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'public/index.html')

def algorithms(request):
    return render(request, 'public/algorithms.html')

def workflows(request):
    return render(request, 'public/workflows.html')

def author(request):
    return HttpResponse("Hello in the authors page")