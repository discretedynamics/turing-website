from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from public.models import Algorithm

# Create your views here.
def launch(request):
    return HttpResponse('Helllloooo from algopiper app')


