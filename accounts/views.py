from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                context['errors'].append("Username already taken")
                return render(request, 'accounts/register.html', context)
            else:
                if User.objects.filter(email=email).exists():
                    context['errors'].append("Email already taken")
                    return render(request, 'accounts/register.html', context)
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    login(request, user)
                    return redirect('home:home')
        else:
            context['errors'].append("Passwords do not match")
            return render(request, "accounts/register.html", context)
    return render(request, 'accounts/register.html')


def auth_login(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
    return render(request, 'accounts/login.html')


def auth_logout(request):
    logout(request)
    return redirect('home:home')
