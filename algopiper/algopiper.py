import docker
from .models import RunningAlgoPiper
from algorun.models import RunningContainer
from socket import *
from django.shortcuts import get_object_or_404
from django.conf import settings
import threading


def clean_algopiper_containers():
    running_containers_list = RunningAlgoPiper.objects.all()
    for running_container in running_containers_list:
        if running_container.time_to_delete():
            remove_container(running_container.container_id)


def clean_algorithm_containers():
    running_containers_list = RunningContainer.objects.all()
    for running_container in running_containers_list:
        if running_container.time_to_delete():
            remove_container(running_container.container_id)


def get_random_port():
    ip = 'localhost'

    # this range contains dynamic or private ports that cannot be registered with IANA.[202] This range is used
    # for private, or customized services or temporary purposes and for automatic allocation of ephemeral ports.
    for i in range(49152, 65535):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.020)
        result = s.connect_ex((ip, i))
        if result != 0:
            s.close()
            return i
        s.close()


def remove_container(container_id):
    client = docker.from_env()
    try:
        client.containers.get(container_id).stop()
        client.containers.get(container_id).remove()

        running_container = get_object_or_404(RunningContainer, container_id=container_id)
        running_container.delete()

        response = {'success': True, \
                    'response': "Deleted Successfully"}
        return response
    except Exception as e:
        response = {'success': False, \
                    'response': e.message}
        return response


def run_algopiper(visitor_id, workflow_name=None, workflow_file=None):
    client = docker.from_env()

    # clean containers that have been running for more than 12 hours
    thr = threading.Thread(target=clean_algopiper_containers, args=(), kwargs={})
    thr.start()

    docker_image = 'algorun/algopiper'
    algo_manager = getattr(settings, "ALGOMANAGER", None)
    env_variables = {"MANAGER": algo_manager}

    if workflow_file and workflow_name:
        env_variables['PIPELINE_URL'] = workflow_file
        env_variables['PIPELINE_NAME'] = workflow_name

    try:
        port = get_random_port()
        container = client.containers.run(str(docker_image), detach=True,ports={8765: port}, \
                                          environment=env_variables)

        new_container = RunningAlgoPiper(visitor_id=visitor_id, \
                                         container_id=container.id, \
                                         port_number=port)
        new_container.save()
        response = {'success': True, \
                    'response': port}
        return response
    except Exception as e:
        response = {'success': False, \
                    'response': e.message}
        return response


def run_container(docker_image, visitor_id):
    client = docker.from_env()

    # clean containers that have been running for more than 12 hours
    thr = threading.Thread(target=clean_algorithm_containers, args=(), kwargs={})
    thr.start()

    try:
        port = get_random_port()
        container = client.containers.run(str(docker_image), detach=True,ports={8765: port})
        new_container = RunningContainer(visitor_id=visitor_id, \
                                         docker_image=docker_image, \
                                         container_id=container.id, \
                                         port_number=port)
        new_container.save()
        response = {'success': True, \
                    'response': port}
        return response
    except Exception as e:
        response = {'success': False, \
                    'response': e.message}
        return response