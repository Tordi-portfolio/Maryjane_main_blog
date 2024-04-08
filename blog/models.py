from django.db import models
from datetime import datetime

class Post(models.Model):
    topic = models.CharField(max_length=100)
    content = models.TextField()
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.topic
