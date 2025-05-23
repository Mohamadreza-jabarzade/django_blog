from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100,default='Mohamadreza')

    def __str__(self):
        return self.title
