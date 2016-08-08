from django.http import HttpResponse
from algorun import run_container, remove_container


def launch(request):
    docker_image = request.GET.get('docker_image', None)
    result = run_container(docker_image, 'VISITOOOOR')
    return HttpResponse(result['response'])
