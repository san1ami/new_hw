from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

from  users.models import CustomUser
from users.forms import CustomUserForm


def user_list_view(request):
    if request.method == 'GET':
        users_list = CustomUser.objects.all().order_by('-id')
        return render(
            request,
            'users/user_list.html',
            {
                'users_list': users_list
            }
        )
# выход
def auth_logout_view(request):
    logout(request)
    return redirect('login')




def auth_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # ← ВАЖНО
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users_list')  # или куда нужно
    else:
        form = AuthenticationForm()

    return render(
        request,
        'users/login.html',
        {'form': form}
    )


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Регистрация прошла успешно 200')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render (
        request, 
        'users/create_user.html',
        {
            "form": form
        }
    )