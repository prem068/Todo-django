from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from app.forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
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
    task = Task.objects.get(id=task_id)   
    f = TaskForms(instance=task)  
    if request.method == 'POST':
        f = TaskForms(request.POST, instance=task)  
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    d = {'forms': f, 'task': task}
    return render(request, 'taskform.html', d)
    
#api-calls
@api_view(['GET'])
def api_get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def api_update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return Response({'message': 'Task deleted successfully'}, status=204)