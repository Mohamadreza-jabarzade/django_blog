from django.shortcuts import render, get_object_or_404

from blog.models import Post
from django.shortcuts import render
from .models import Post  # فرض بر اینکه مدل Post داری

def home(request):
    top_posts = Post.objects.order_by('created_at')[:3]  # یا هر شرط دلخواه
    return render(request, 'home.html', {'top_posts': top_posts})

def about(request):
    return render(request, 'about.html')

def posts(request):
    # اگر دوتا صفحه متفاوت می‌خوای می‌تونی تغییر بدی
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})

def contact(request):
    return render(request, 'contact.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})