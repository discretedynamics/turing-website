from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Algorithm
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