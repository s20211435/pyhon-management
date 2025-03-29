from django.contrib.auth.decorators import user_passes_test  # 修正
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import CustomUserCreationForm


User = get_user_model()

# 管理者チェックデコレーター
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ユーザーを作成しました。')
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_form.html', {'form': form})

# @user_passes_test(is_admin)
# def user_edit(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'ユーザーを更新しました。')
#             return redirect('user_list')
#     else:
#         form = UserCreationForm(instance=user)
#     return render(request, 'users/user_form.html', {'form': form, 'user': user})

@user_passes_test(lambda u: u.is_superuser)  # 管理者のみアクセス可能
def user_edit_ajax(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = UserCreationForm(instance=user)

    # フォームをHTMLとしてレンダリング
    html = render_to_string('users/user_form.html', {'form': form}, request=request)
    return JsonResponse({'success': False, 'html': html})

@user_passes_test(is_admin)
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'ユーザーを削除しました。')
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})

# 管理者専用ビュー
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

# 一般ユーザー専用ビュー
@user_passes_test(lambda u: not u.is_superuser)
def user_dashboard(request):
    return render(request, 'users/user_dashboard.html')

def redirect_after_login(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')