from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'new_contributors': 1, \
               'new_algorithms': 2, \
               'new_workflows': 3, \
               }
    return render(request, 'public/index.html', context)

def algorithms(request):
    return render(request, 'public/algorithms.html')

def workflows(request):
    return render(request, 'public/workflows.html')

def contribute(request):
    return HttpResponse("Hello in the contribute page")

def about(request):
    return HttpResponse("Hello in the about page")