from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from app.forms import *
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html',{'tasks':tasks})

def toggle_complete(request, task_id):

    task = Task.objects.get(id=task_id)

    task.completed = not task.completed
    task.save()

    return redirect('index')

def task_delete(request, task_id):

    task = Task.objects.get(id=task_id)

    task.delete()

    return redirect('index')

def insert_task(request):
    f=TaskForms()
    if request.method=='POST':
        f=TaskForms(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'forms':f}
    return render(request,'taskform.html',d)

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task 
    f = TaskForms(instance=task)  # Pre-fill the form with the task data
    if request.method == 'POST':
        f = TaskForms(request.POST, instance=task)  # Bind the form with POST data
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    d = {'forms': f, 'task': task}
    return render(request, 'taskform.html', d)
    