import os
from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from openai.types.chat.chat_completion import ChatCompletion
from pytubefix import YouTube
from django.conf import settings
import assemblyai as aai
import openai
from pytubefix.streams import Stream
from .models import BlogPost

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
    print(title)
    audio_file = download_audio(youtube_data)
    print(audio_file)
    transcription = get_transcription(audio_file)    
    if not transcription:
        return JsonResponse({'error': 'Transcription failed'}, status=500)
    
    blog_content = generate_blog_text(transcription)
    if not blog_content:
        return JsonResponse({'error': 'Blog generation failed'}, status=500)
    
    BlogPost.objects.create(
        youtube_title=title,
        youtube_link=youtube_link, 
        content=blog_content, 
        author=request.user,
    )
    
    return JsonResponse({"content": blog_content})   

def download_audio(youtube_data: YouTube) -> str:
    # check if file already exists on disk
    expected_path: str = os.path.join(settings.MEDIA_ROOT, youtube_data.title + '.mp3')
    if os.path.exists(expected_path):
        return expected_path
    
    audio_file: Stream = youtube_data.streams.filter(only_audio=True).first()
    out_file: str = audio_file.download(output_path=settings.MEDIA_ROOT)
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

    with open('transcript.txt', 'w') as f:
        f.write(transcript.text)
    return transcript.text

def generate_blog_text(transcription) -> str:
    openai.api_key = get_openai_api_key()

    client = openai.OpenAI()
    
    prompt: str = f"Based on the following transcript from a YouTube video, write a comprehensive blog article, write it based on the transcript, but dont make it look like a youtube video, make it look like a proper blog article:\n\n{transcription}\n\nArticle:"

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000
    )

    generated_blog: str = completion.choices[0].message.content.strip()
    
    return generated_blog

def blog_list(request) -> HttpResponse:
    blogs: BaseManager[BlogPost] = BlogPost.objects.filter(author=request.user).order_by('-date_posted')
    return render(request, 'all-blogs.html', {'blog_posts': blogs})
    
def user_login(request) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user: AbstractUser | None = authenticate(username=username, password=password)
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