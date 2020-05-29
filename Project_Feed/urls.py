"""Project_Feed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include,path
# from ProjectFeed.views import index
from django.conf import settings
# import ProjectFeed.urls
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('ProjectFeed.urls')),
    path('',TemplateView.as_view(template_name="index.html"),name="index"),
    path('about',TemplateView.as_view(template_name="about.html"),name="about"),
    path('roulette',TemplateView.as_view(template_name="roulette.html"),name="roulette"),
    path('signin',TemplateView.as_view(template_name="signin.html"),name="signin"),
    path('signup',TemplateView.as_view(template_name="signup.html"),name="signup"),


]
