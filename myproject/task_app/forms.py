# filepath: c:\docker_code\myproject\todo_app\forms.py
from django import forms
from .models import Task  # Todo から Task に変更

class TaskForm(forms.ModelForm):  # TodoForm から TaskForm に変更
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'user_id', 'parent_task_id']
