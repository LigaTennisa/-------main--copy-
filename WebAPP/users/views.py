import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm

base_api_url = getattr(settings, 'BASE_API_URL', '')


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            response = requests.post(
                f'{base_api_url}/users/', json={
                    'email': user.email,
                    'last_name': user.last_name,
                    'first_name': user.first_name,
                    'password1': form.cleaned_data['password1'],
                    'password2': form.cleaned_data['password2'],
                })
            if response.status_code != 201:
                messages.error(request, response.json().get('detail', 'Ошибка'))
                return render(request, 'users/register.html', {'form': form})

            user.save()
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'users/register.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']  # Изменяем на email
            password = form.cleaned_data['Пароль']
            # Используем email вместо username
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('posts')

        messages.error(request, f'Неверный email или пароль')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    # messages.success(request, f'You have been logged out.')
    return redirect('home')


def home(request):
    return render(request, 'home.html')
