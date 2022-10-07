from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tasks.models import Task


def index(request):
    return HttpResponse("Hello, world. You're at the task index.")

def create(request):
    return HttpResponse("Hello, world. You're at the task create screen.")

def list(request):
    tasks_list = Task.objects.all
    context = {'tasks_list': tasks_list}
    template = loader.get_template("tasks/list.html")
    return render(request, 'tasks/list.html', context)

def edit(request, task_id):
    return HttpResponse("Hello, world. You're at the edit screen for task %s." % task_id)