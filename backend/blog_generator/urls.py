from django.urls import path
from django.urls.resolvers import URLPattern
from blog_generator import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns: list[URLPattern] = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('generate-blog', views.generate_blog, name='generate-blog'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog-details/<int:pk>/', views.blog_details, name='blog-details'),
    path('delete-blog/<int:pk>/', views.delete_blog, name='delete-blog'),
]
