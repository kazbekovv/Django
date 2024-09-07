from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"



