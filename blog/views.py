from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from blog.models import Post
from django.contrib import messages
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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد!')
            return redirect('login')
        else:
            messages.error(request, 'خطایی در اطلاعات وارد شده وجود دارد.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})