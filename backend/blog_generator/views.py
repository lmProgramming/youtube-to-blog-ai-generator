from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# Create your views here.
def index(request) -> HttpResponse:
    return render(request, 'index.html')

def user_login(request) -> HttpResponse:
    return render(request, 'login.html')

def user_signup(request) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeatPassword')
        
        if password != repeat_password:
            error_message = 'Passwords do not match'
            return render(request, 'signup.html', {'error_message': error_message})
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('/')
        except:
            error_message = 'Username already exists'
            return render(request, 'signup.html', {'error_message': error_message})            
    return render(request, 'signup.html')

def user_logout(request) -> HttpResponse:
    pass