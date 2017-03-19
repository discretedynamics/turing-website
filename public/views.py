from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Algorithm, Contributor, Workflow
import ast
from django.views.decorators.csrf import csrf_exempt
import logging


# Create your views here.
def home(request):
    context = {'new_contributors': 1, \
               'new_algorithms': 2, \
               'new_workflows': 3, \
               }
    if not request.user.is_authenticated():
        return render(request, 'public/index.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.email)
    context['contributor'] = contributor
    return render(request, 'public/index.html', context)


def algorithms(request):
    algorithms_list = Algorithm.objects.filter(status='published')
    context = {
        'algorithms_list': algorithms_list
    }
    if not request.user.is_authenticated():
        return render(request, 'public/algorithms.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.email)
    context['contributor'] = contributor
    return render(request, 'public/algorithms.html', context)


def useAlgorithm(request, algorithm_id):
    algorithm = get_object_or_404(Algorithm, pk=algorithm_id)
    versions = ast.literal_eval(algorithm.versions)
    context = { 'algorithm': algorithm, \
                'versions': versions}

    if not request.user.is_authenticated():
        return render(request, 'public/algorithm.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.email)
    context['contributor'] = contributor
    return render(request, 'public/algorithm.html', context)


def workflows(request):
    workflows_list = Workflow.objects.filter(status='published')
    context = {
        'workflows_list': workflows_list
    }

    if not request.user.is_authenticated():
        return render(request, 'public/workflows.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.email)
    context['contributor'] = contributor
    return render(request, 'public/workflows.html', context)


def contribute(request):
    if not request.user.is_authenticated():
        return render(request, 'public/contribute.html')
    contributor = get_object_or_404(Contributor, email=request.user.email)
    context = {'contributor': contributor}
    return render(request, 'public/contribute.html', context)


def about(request):
    if not request.user.is_authenticated():
        return render(request, 'public/about.html')
    contributor = get_object_or_404(Contributor, email=request.user.email)
    context = {'contributor': contributor}
    return render(request, 'public/about.html', context)


def faq(request):
    if not request.user.is_authenticated():
        return render(request, 'public/faq.html')
    contributor = get_object_or_404(Contributor, email=request.user.email)
    context = {'contributor': contributor}
    return render(request, 'public/faq.html', context)


def user_guide(request):
    if not request.user.is_authenticated():
        return render(request, 'public/faq.html')
    contributor = get_object_or_404(Contributor, email=request.user.email)
    context = {'contributor': contributor}
    return render(request, 'public/faq.html', context)


def contact(request):
    if not request.user.is_authenticated():
        return render(request, 'public/contact.html')
    contributor = get_object_or_404(Contributor, email=request.user.email)
    context = {'contributor': contributor}
    return render(request, 'public/contact.html', context)


def signup(request):
    if not request.user.is_authenticated():
        return render(request, 'public/signup.html')
    return redirect('public:home')


def validate_signup_form(request):
    context = {}
    form_complete = True

    name  = request.POST.get('name', '')
    if name is not None:
        context['name'] = name
    else:
        context['missing_name'] = 'has-error'
        form_complete = False

    email  = request.POST.get('email', '')
    if email is not None:
        context['email'] = email
    else:
        context['missing_email'] = 'has-error'
        form_complete = False

    organization  = request.POST.get('organization', '')
    if organization is not None:
        context['organization'] = organization
    else:
        context['missing_organization'] = 'has-error'
        form_complete = False

    password = request.POST.get('password', '')
    if password is not None:
        context['password'] = password
    else:
        context['missing_password'] = 'has-error'
        form_complete = False
    confirm_password  = request.POST.get('confirm_password', '')
    if confirm_password is not None:
        context['confirm_password'] = confirm_password
    else:
        context['missing_password'] = 'has-error'
        form_complete = False

    if form_complete:
        if context['password'] != context['confirm_password']:
            context['password_error'] = 'has-error'
            form_complete = False

    return form_complete, context

def signup_submit(request):

    form_complete, context = validate_signup_form(request)

    if form_complete:
        try:
            user = User.objects.get(username=context['email'])
            # user exists!
            context = {'error_message': "This email address already exists! Please, sign in instead!"}
            return render(request, 'public/signup.html', context)
        except User.DoesNotExist:
            user = User.objects.create_user(username=context['email'], \
                                            email=context['email'], \
                                            password=context['password'])
            user.save()
            new_contributor = Contributor(name=context['name'], \
                                          email=context['email'], \
                                          organization=context['organization'])
            new_contributor.save()
            user = auth.authenticate(username=context['email'], password=context['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('contributor:profile')

def signin(request):
    if not request.user.is_authenticated():
        return render(request, 'public/signin.html')
    return redirect('contributor:profile')


def signin_submit(request):
    username = request.POST['email']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('contributor:profile')
    else:
        context = {'error_message': 'Invalid credentials!', \
                   'wrong_email': 'has-error', \
                   'wrong_password': 'has-error'}
        return render(request, 'public/signin.html', context)


def sign_out(request):
    auth.logout(request)
    return redirect('public:home')