from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) -> HttpResponse:
    return render(request, 'index.html')

def user_login(request) -> HttpResponse:
    return render(request, 'login.html')

def user_signup(request) -> HttpResponse:
    return render(request, 'signup.html')

def user_logout(request) -> HttpResponse:
    pass