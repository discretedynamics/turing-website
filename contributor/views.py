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


def algorithms_how_to(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    context = {'contributor': contributor}
    return render(request, 'contributor/algorithms-how-to.html', context)


def my_algorithms(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    algorithms = Algorithm.objects.filter(contributor=contributor)
    submitted_algorithms = []
    published_algorithms = []
    for algorithm in algorithms:
        if algorithm.status == 'pending':
            submitted_algorithms.append(algorithm)
        else:
            published_algorithms.append(algorithm)

    context = {'contributor': contributor, \
               'submitted_algorithms': submitted_algorithms, \
               'published_algorithms': published_algorithms}
    return render(request, 'contributor/algorithms-my-algorithms.html', context)


def submit_algorithm(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    context = {'contributor': contributor}
    return render(request, 'contributor/algorithms-submit-algorithm.html', context)

@csrf_protect
def submit_algorithm_info(request):
    contributor = get_object_or_404(Contributor, email=request.user.email)
    new_algorithm = Algorithm()
    new_algorithm.docker_image = request.POST.get('docker', '')
    new_algorithm.contributor = contributor
    if not new_algorithm.docker_image:
        messages.add_message(request, messages.ERROR, "You must specify the name of your Docker image on Docker Hub!")
        return redirect('contributor:submit-algorithm')
    new_algorithm.save()
    messages.add_message(request, messages.INFO, "We received your submission. \
                                                 You will receive an email once it is available on our server.")
    return redirect('contributor:submit-algorithm')

