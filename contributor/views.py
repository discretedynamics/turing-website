from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from public.models import Algorithm, Contributor, Workflow
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


# Algorithms

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
        if algorithm.status == 'pending' or algorithm.status == 'unpublished':
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


@csrf_protect
def delete_algorithm(request, algorithm_id):
    algorithm = get_object_or_404(Algorithm, id=algorithm_id)
    algorithm.delete()
    return redirect('contributor:my-algorithms')


@csrf_protect
def unpublish_algorithm(request, algorithm_id):
    algorithm = get_object_or_404(Algorithm, id=algorithm_id)
    algorithm.status = 'unpublished'
    algorithm.save()
    return redirect('contributor:my-algorithms')


@csrf_protect
def submit_new_version(request, algorithm_id):
    algorithm = get_object_or_404(Algorithm, id=algorithm_id)
    version = request.GET.get('version', None)
    algorithm.new_version = version
    algorithm.save()

    messages.add_message(request, messages.INFO, "Your algorithm new version will be available on our servers shortly.")
    return redirect('contributor:my-algorithms')


# Workflows

def workflows_how_to(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    context = {'contributor': contributor}
    return render(request, 'contributor/workflows-how-to.html', context)


def my_workflows(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    workflows = Workflow.objects.filter(contributor=contributor)
    submitted_workflows = []
    published_workflows = []
    for workflow in workflows:
        if workflow.status == 'pending' or workflow.status == 'unpublished':
            submitted_workflows.append(workflow)
        else:
            published_workflows.append(workflow)

    context = {'contributor': contributor, \
               'submitted_workflows': submitted_workflows, \
               'published_workflows': published_workflows}
    return render(request, 'contributor/workflows-my-workflows.html', context)


def submit_workflow(request):
    if not request.user.is_authenticated():
        context = {'error_message': 'Please, sign in!'}
        return render(request, 'public/signin.html', context)

    contributor = get_object_or_404(Contributor, email=request.user.username)
    context = {'contributor': contributor}
    return render(request, 'contributor/workflows-submit-workflow.html', context)


@csrf_protect
def submit_workflow_json(request):
    contributor = get_object_or_404(Contributor, email=request.user.email)
    new_workflow = Workflow()
    new_workflow.name = request.POST.get('workflow_name', '')
    new_workflow.description = request.POST.get('workflow_description', '')
    new_workflow.workflow_json = request.POST.get('workflow_json', '')
    new_workflow.contributor = contributor

    context = {'name': new_workflow.name, \
               'description': new_workflow.description, \
               'json': new_workflow.workflow_json }

    if not new_workflow.name:
        messages.add_message(request, messages.ERROR, "You must specify the name of your workflow!")
        return render(request, 'contributor/workflows-submit-workflow.html', context)
    if not new_workflow.description:
        messages.add_message(request, messages.ERROR, "You must provide a description for your workflow!")
        return render(request, 'contributor/workflows-submit-workflow.html', context)
    if not new_workflow.workflow_json:
        messages.add_message(request, messages.ERROR, "You must provide the JSON definition of your workflow!")
        return render(request, 'contributor/workflows-submit-workflow.html', context)

    new_workflow.save()
    messages.add_message(request, messages.INFO, "We received your submission. \
                                                 You will receive an email once it is available on our server.")
    return redirect('contributor:submit-workflow')


@csrf_protect
def delete_workflow(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)
    workflow.delete()
    return redirect('contributor:my-workflows')


@csrf_protect
def unpublish_workflow(request, workflow_id):
    workflow = get_object_or_404(Workflow, id=workflow_id)
    workflow.status = 'unpublished'
    workflow.save()
    return redirect('contributor:my-workflows')