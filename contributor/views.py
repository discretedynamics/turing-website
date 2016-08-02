from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from public.models import Algorithm, Contributor
import ast
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


# Create your views here.


def profile(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    context = {'contributor': contributor}
    return render(request, 'contributor/profile.html', context)


@csrf_protect
def update_profile(request):
    contributor = get_object_or_404(Contributor, email=request.user.email)
    contributor.name = request.POST.get('name', '')
    contributor.email = request.POST.get('email', '')
    user = User.objects.get(username=request.user.email)
    user.email = contributor.email
    user.username = contributor.email
    user.save()
    contributor.personal_website = request.POST.get('personal_website', '')
    contributor.organization = request.POST.get('organization', '')
    contributor.organization_website = request.POST.get('organization_website', '')
    contributor.save()

    messages.add_message(request, messages.INFO, "Profile updated successfully")
    return redirect('contributor:profile')
