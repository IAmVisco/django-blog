from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
