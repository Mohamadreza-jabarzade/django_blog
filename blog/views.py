from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ContactForm
from blog.models import Post
from django.contrib import messages
from django.shortcuts import render
from .models import Post
from .forms import CommentForm

def home(request):
    top_posts = Post.objects.order_by('created_at')[:3]  # یا هر شرط دلخواه
    return render(request, 'home.html', {'top_posts': top_posts})


def posts(request):
    # اگر دوتا صفحه متفاوت می‌خوای می‌تونی تغییر بدی
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

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

@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'total_likes': post.total_likes()
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # این خط داده‌ها رو در دیتابیس ذخیره می‌کنه ✅
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
