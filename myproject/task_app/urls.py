# filepath: c:\docker_code\myproject\todo_app\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # todo_list から task_list に変更
    path('create/', views.task_create, name='task_create'),  # todo_create から task_create に変更
    path('update/<int:pk>/', views.task_update, name='task_update'),  # todo_update から task_update に変更
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),  # todo_delete から task_delete に変更
]