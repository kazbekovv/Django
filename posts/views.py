from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from posts.models import Post, Comment, Tag
from posts.forms import PostForm2, CommentForm, SearchForm
import random
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, CreateView, DetailView


def test_view(request):
    return HttpResponse(f"Охх! {random.randint(1, 100)}")

class TestView(View):
    def get (self, request):
        return HttpResponse(f"Охх! {random.randint(1, 100)}")

def main_page_view(request):
    return render(request, 'base.html')

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    form_class = SearchForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        tag = self.request.GET.getlist('tag')
        posts = Post.objects.all()
        if search:
            post = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tag:
            posts = posts.filter(tags__id__in=tag)



@login_required(login_url="login")
def post_list_view(request):
    if request.method == 'GET':
        form = SearchForm()
        posts = Post.objects.all()
        search = request.GET.get('search')
        tag = request.GET.getlist('tag')
        ordering = request.GET.get('ordering')
        if search:
            post = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tag:
            posts = posts.filter(tags__id__in=tag)
        if ordering:
            posts = posts.order_by(ordering)
        page = request.GET.get('page', 1)
        page = int(page)
        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages)+1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]
        context = {'posts': posts, 'form': form, "max_pages": range(1, max_pages + 1)}
        return render(request, 'posts/post_list.html', context= context)

class PostCreateView(CreateView):
    model =Post
    template_name = 'posts/post_create.html'
    form_class = PostForm2
    success_url = "/posts2/"
    
class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
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

def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        form = PostForm2(instance=post)
        return render(request, 'posts/post_update.html', context={'post': post, 'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_update.html', context={'post': post, 'form': form})
        form.save()
        return redirect("/profile/")