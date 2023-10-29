from django.db import models
from datetime import datetime

CREATED = 'created'
UPDATED = 'updated'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    counter = models.PositiveIntegerField(default=0)
    cotegoru = models.TextField(max_length=200, default='')
    created_at = models.DateTimeField(default=datetime.now)


class Comment(models.Model):
    CREATED = 'created'
    UPDATED = 'updated'
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=100, default=CREATED)



