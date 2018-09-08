"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import PostListView
from core.views import signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/',
         auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                      template_name='registration/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('signup/', signup_view, name='signup'),
]
