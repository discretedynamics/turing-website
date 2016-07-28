from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Algorithm, Contributor

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
    context = { 'algorithm': algorithm }
    return render(request, 'public/algorithm.html', context)



def workflows(request):
    workflows_list = [{'id': 1, 'name': 'Workflow 1', 'description': 'desc1'}, \
                       {'id': 2, 'name': 'Workflow 2', 'description': 'desc2'}, \
                       {'id': 3, 'name': 'Workflow 3', 'description': 'desc3'}, \
                       {'id': 4, 'name': 'Workflow 4', 'description': 'desc4'}]
    context = {
        'workflows_list': workflows_list
    }
    return render(request, 'public/workflows.html', context)


def runWorkflow(request, workflow_id):
    context = { 'workflow': {'id': workflow_id, \
               'name': 'ay 7aga delwa2t' + str(workflow_id)} }
    return render(request, 'public/workflow.html', context)

def contribute(request):
    return HttpResponse("Hello in the contribute page")

def about(request):
    return HttpResponse("Hello in the about page")

def faq(request):
    return HttpResponse("Hello in the FAQ page")

def contact(request):
    return HttpResponse("Hello in the contact page")