from django.urls import path
from django.urls.resolvers import URLPattern
from blog_generator import views

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
]