from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class GetObjectMixin():
    def get_object(self, *args, **kwargs):
        return get_object_or_404(Post, id=self.kwargs.get("id"))


class PostListView(GetObjectMixin, ListView):
    model = Post


class PostDetailView(GetObjectMixin, DetailView):
    model = Post


class PostCreateView(GetObjectMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm


class PostUpdateView(GetObjectMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form_update.html'
