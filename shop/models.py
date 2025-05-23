from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    video = models.FileField(upload_to='courses/videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
