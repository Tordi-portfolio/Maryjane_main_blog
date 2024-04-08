from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def base(request):
    return render(request, 'base.html')

def bio(request):
    return render(request, 'bio.html')

def home(request):
    return render(request, 'home.html')