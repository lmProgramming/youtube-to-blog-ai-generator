from django.urls import path
from django.urls.resolvers import URLPattern
from blog_generator import views

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='index'),
    path('signup', views.user_signup, name='index'),
    path('logout', views.user_logout, name='index'),
]