from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

from .models import Secret
from .forms import SecretForm
from .forms import RegistrationForm
import random

def home(request):
    return render(request, 'home.html')


@login_required
def protected_view(request):
    return render(request, 'protected.html')

@login_required
def get_random_secret(request):
    # Получаем все записи из модели Secret
    secrets = list(Secret.objects.all())

    if secrets:
        random_secret = random.choice(secrets)
        return JsonResponse({'secret': random_secret.text})
    else:
        return JsonResponse({"error": "Нет записей в базе данных"})



def secret_page(request):
    if request.method == 'POST':
        form = SecretForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Секрет сохранен'
            context = {'form': SecretForm(), 'message': message}
            return render(request, 'secret.html', context)
    else:
        form = SecretForm()

    context = {'form': form}
    return render(request, 'secret.html', context)




def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = f'Приветствую, {username}'
            context = {'message': message}
            return render(request, 'home.html', context)
        else:
            message = 'Неверный логин или пароль'
            context = {'message': message}
            return render(request, 'login.html', context)
    return render(request, 'login.html')



def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return redirect('/')