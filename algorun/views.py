from django.http import HttpResponse
from django.shortcuts import render
from algorun import run_container
from models import RunningContainer
import uuid
import json


def launch(request):
    docker_image = request.GET.get('docker_image', None)
    if 'visitor' in request.COOKIES:
        visitor = request.COOKIES['visitor']
        print 'old visitor'
    else:
        visitor = uuid.uuid4()
        print 'new visitor'

    # check to see if there is a running container for that user with the same docker image
    try:
        running_container = RunningContainer.objects.get(visitor_id=visitor, docker_image=docker_image)
    except RunningContainer.DoesNotExist:
        running_container = None

    if running_container:
        result = {'success': True, \
                  'response': running_container.port_number}
    else:
        result = run_container(docker_image, visitor)

    response = HttpResponse(json.dumps(result))
    response.set_cookie('visitor', visitor)

    return response


def view_algorithm_page(request, port_number):
    context = {'port': port_number}
    return render(request, 'algorun/view_algorithm.html', context)