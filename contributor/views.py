from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from public.models import Algorithm, Contributor
import ast
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def profile(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.email)
    context = {'contributor': contributor}
    return render(request, 'contributor/profile.html', context)