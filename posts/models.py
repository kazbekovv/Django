from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='posts/')
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')