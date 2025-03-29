from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # 修正: ベースURLでユーザー一覧を表示
    path('create/', views.user_create, name='user_create'),
    path('<int:user_id>/edit/ajax/', views.user_edit_ajax, name='user_edit_ajax'),
    path('<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]