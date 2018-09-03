from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('create/', PostCreateView.as_view(), name='blog-create'),
]
