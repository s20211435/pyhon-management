# filepath: c:\docker_code\myproject\todo_app\views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # TodoForm から TaskForm に変更

def task_list(request):  # todo_list から task_list に変更
    tasks = Task.objects.all()  # todos から tasks に変更
    return render(request, 'task_app/task_list.html', {'tasks': tasks})  # todo_list.html から task_list.html に変更

def task_create(request):  # todo_create から task_create に変更
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # todo_list から task_list に変更
    else:
        form = TaskForm()
    return render(request, 'task_app/task_form.html', {'form': form})  # todo_form.html から task_form.html に変更

def task_update(request, pk):  # todo_update から task_update に変更
    task = get_object_or_404(Task, pk=pk)  # todo から task に変更
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # todo_list から task_list に変更
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_app/task_form.html', {'form': form})  # todo_form.html から task_form.html に変更

def task_delete(request, pk):  # todo_delete から task_delete に変更
    task = get_object_or_404(Task, pk=pk)  # todo から task に変更
    if request.method == "POST":
        task.delete()
        return redirect('task_list')  # todo_list から task_list に変更
    return render(request, 'task_app/task_confirm_delete.html', {'task': task})  # todo_confirm_delete.html から task_confirm_delete.html に変更