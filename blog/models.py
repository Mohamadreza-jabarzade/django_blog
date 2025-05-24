from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100,default='Mohamadreza')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    course = models.ForeignKey('shop.Course', on_delete=models.CASCADE, null=True, blank=True)

    def total_likes(self):
        return self.likes.count()
    total_likes.short_description = 'تعداد لایک‌ها'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="متن کامنت")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.content[:30]}"