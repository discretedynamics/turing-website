from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, Http404
from .models import Algorithm, Contributor
import ast


# Create your views here.
def home(request):
    context = {'new_contributors': 1, \
               'new_algorithms': 2, \
               'new_workflows': 3, \
               }
    return render(request, 'public/index.html', context)


def algorithms(request):
    algorithms_list = Algorithm.objects.order_by('-pub_date')[:5]
    context = {
        'algorithms_list': algorithms_list
    }
    return render(request, 'public/algorithms.html', context)


def useAlgorithm(request, algorithm_id):
    algorithm = get_object_or_404(Algorithm, pk=algorithm_id)
    versions = ast.literal_eval(algorithm.versions)
    context = { 'algorithm': algorithm, \
                'versions': versions}
    return render(request, 'public/algorithm.html', context)


def workflows(request):
    workflows_list = []
    context = {
        'workflows_list': workflows_list
    }
    return render(request, 'public/workflows.html', context)


def runWorkflow(request, workflow_id):
    context = { 'workflow': {'id': workflow_id, \
               'name': 'ay 7aga delwa2t' + str(workflow_id)} }
    return render(request, 'public/workflow.html', context)


def contribute(request):
    return render(request, 'public/contribute.html')


def about(request):
    return render(request, 'public/about.html')


def faq(request):
    return render(request, 'public/faq.html')


def contact(request):
    return render(request, 'public/contact.html')


def signup(request):
    return render(request, 'public/signup.html')


def validate_signup_form(request):
    context = {}
    form_complete = True
    if 'name' in request.POST:
        if request.POST['name']:
            context['name'] = request.POST['name']
        else:
            context['missing_name'] = 'has-error'
            form_complete = False
    else:
        context['missing_name'] = 'has-error'
        form_complete = False

    if 'email' in request.POST:
        if request.POST['email']:
            context['email'] = request.POST['email']
        else:
            context['missing_email'] = 'has-error'
            form_complete = False
    else:
        context['missing_email'] = 'has-error'
        form_complete = False

    if 'organization' in request.POST:
        if request.POST['organization']:
            context['organization'] = request.POST['organization']
        else:
            context['missing_organization'] = 'has-error'
            form_complete = False
    else:
        context['missing_organization'] = 'has-error'
        form_complete = False

    if 'password' in request.POST:
        if request.POST['password']:
            context['password'] = request.POST['password']
        else:
            context['password_error'] = 'has-error'
            form_complete = False
    else:
        context['password_error'] = 'has-error'
        form_complete = False

    if 'confirm_password' in request.POST:
        if request.POST['confirm_password']:
            context['confirm_password'] = request.POST['confirm_password']
        else:
            context['password_error'] = 'has-error'
            form_complete = False
    else:
        context['password_error'] = 'has-error'
        form_complete = False

    return form_complete, context


def signup_submit(request):
    form_complete, context = validate_signup_form(request)

    if form_complete:
        new_contributor = Contributor(name=context['name'], \
                                      email=context['email'], \
                                      organization=context['organization'])
        #new_contributor.save()
        return HttpResponse('Sigun will be available very soon!')
    else:
        return render(request, 'public/signup.html', context)


def signin(request):
    return render(request, 'public/signin.html')


def signin_submit(request):
    return HttpResponse('Sign in will be available soon!')

    '''if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")'''


def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")