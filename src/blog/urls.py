from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostUpdateView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-list'),
    path('<int:id>/', PostDetailView.as_view(), name='blog-detail'),
    path('create/', PostCreateView.as_view(), name='blog-create'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='blog-update'),
]
