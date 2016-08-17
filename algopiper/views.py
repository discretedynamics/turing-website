from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from public.models import Algorithm
from algopiper import run_container, run_algopiper
from algorun.models import RunningContainer
from models import RunningAlgoPiper
from django.conf import settings
import ast, json, uuid
from django.apps import apps


# Create your views here.
def manager_list(request):
    available_algorithms = Algorithm.objects.filter(status='published')
    available_images = []
    for algorithm in available_algorithms:
        versions = ast.literal_eval(algorithm.versions)
        for version in versions:
            image = {'name': algorithm.name, \
                     'docker': algorithm.docker_image + ':' + str(version)}
            available_images.append(image)
    result = {'images': json.dumps(available_images)}
    response = HttpResponse(json.dumps(result))

    return response


def manager_deploy(request):
    docker_image = request.POST.get('docker_image', None)
    node_id = request.POST.get('node_id', None)

    if not docker_image or not node_id:
        result = {'status': 'fail',\
                  'error_message': 'missing parameters'}
        return HttpResponse(json.dumps(result))

    # check to see if the node already has a running container
    try:
        running_container = RunningContainer.objects.get(visitor_id=node_id, docker_image=docker_image)
    except RunningContainer.DoesNotExist:
        running_container = None

    server_path = getattr(settings, "SERVER_PATH", None)

    if running_container:
        response = {'status': 'success', \
                    'endpoint': server_path + ":" + str(running_container.port_number)}
        return HttpResponse(json.dumps(response))

    else:
        # check to see if the docker_image is available on the server
        try:
            _ = Algorithm.objects.filter(status='published', docker_image=docker_image)
            result = run_container(docker_image, node_id)
            if result['success']:
                response = {'status': 'success', \
                            'endpoint': server_path + ":" + str(result['response'])}

                return HttpResponse(json.dumps(response))
            else:
                response = {'status': 'fail', \
                            'error_message': result['response']}
                return HttpResponse(json.dumps(response))

        except Algorithm.DoesNotExist:
            result = {'status': 'fail', \
                      'error_message': 'the requested docker image is not available on this server.\
                      use GET /api/v1/list to get all available images.'}
            return HttpResponse(json.dumps(result))


def launch(request):
    if 'visitor' in request.COOKIES:
        visitor = request.COOKIES['visitor']
    else:
        visitor = uuid.uuid4()

    # check to see if there is a running container for that user with the same docker image
    try:
        running_container = RunningAlgoPiper.objects.get(visitor_id=visitor)
    except RunningAlgoPiper.DoesNotExist:
        running_container = None

    if running_container:
        result = {'success': True, \
                  'response': running_container.port_number}
    else:
        result = run_algopiper(visitor)

    response = HttpResponse(json.dumps(result))
    response.set_cookie('visitor', visitor)

    return response


def view_algopiper_page(request, port_number):
    context = {'port': port_number}
    return render(request, 'algopiper/view_algopiper.html', context)