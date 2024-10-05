from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@login_required
def index(request) -> HttpResponse:
    return render(request, 'index.html')

@csrf_exempt
def generate_blog(request) -> HttpResponse:
    if request.method == "POST":
        pass
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def user_login(request) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is None:    
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
        
        login(request, user)
        return redirect('/')
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
    logout(request)
    return redirect('/')