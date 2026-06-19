from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)
        return redirect('/')

    return render(request, 'index.html', {'tasks': tasks})


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('/')

    return render(request, 'update.html', {'task': task})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


