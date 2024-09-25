from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from posts.models import Post, Comment
from posts.forms import PostForm2, CommentForm
import random
from django.contrib.auth.decorators import login_required

def test_view(request):
    return HttpResponse(f"Охх! {random.randint(1, 100)}")

def main_page_view(request):
    return render(request, 'base.html')


@login_required(login_url="login")
def post_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', context={'posts': posts})

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'GET':
        form = CommentForm()
        return render(request, 'posts/post_detail.html', context={'post': post, 'form': form, 'comments': comments})  # Fixed typo in 'comments'
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if not form.is_valid():
            return render(request, 'posts/post_detail.html', context={'post': post, 'form': form, 'comments': comments})  # Include comments for re-rendering
        text = form.cleaned_data['text']
        Comment.objects.create(text=text, post=post)
        return redirect(f"/posts/{post.id}/")

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm2()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        form.save()
        return redirect("/posts/")
