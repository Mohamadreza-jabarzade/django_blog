from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]