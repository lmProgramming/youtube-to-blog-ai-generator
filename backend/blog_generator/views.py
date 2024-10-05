import os
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import YouTube
from django.conf import settings
import assemblyai as aai

@login_required
def index(request) -> HttpResponse:
    return render(request, 'index.html')

def youtube_title(link: str) -> str:
    yt = YouTube(link)
    return yt.title

@csrf_exempt
def generate_blog(request) -> HttpResponse:
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body)
        youtube_link = data['link'] 
        
    except (KeyError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid request body'}, status=400)  
    
    youtube_data = YouTube(youtube_link)
    title: str = youtube_data.title
    audio_file = download_audio(youtube_data)
    transcription = get_transcription(audio_file)
    
    if not transcription:
        return JsonResponse({'error': 'Transcription failed'}, status=500)
    
    return JsonResponse({"content": youtube_link})   

def download_audio(youtube_data) -> str:
    audio_file = youtube_data.streams.filter(only_audio=True).first()
    out_file = audio_file.download(output_path=settings.MEDIA_ROOT)
    base: str = os.path.splitext(out_file)[0]
    new_file: str = base + ".mp3"
    os.rename(out_file, new_file)
    return new_file

def get_assembly_ai_api_key() -> str:
    return open('api_keys/assembly_ai_api_key').read().strip()

def get_openai_api_key() -> str:
    return open('api_keys/openai_api_key').read().strip()
    
def get_transcription(audio_file) -> str:
    aai.settings.api_key = get_assembly_ai_api_key()
    transcriber = aai.Transcriber()

    transcript: aai.Transcript = transcriber.transcribe(audio_file)

    return transcript.text
    
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