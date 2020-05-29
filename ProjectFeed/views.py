from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Location, Features, Profile, Reviews, Comments, Category
from .serializers import (
    LocationSerializer,
    FeaturesSerializer,
    ProfileSerializer,
    ReviewsSerializer,
    CommentsSerializer,
    CategorySerializer,
)
from .forms import *

# Create your views here.

def index(request):
    context = {
        'locations': []
    }
    return render(request, 'locations.html', context)


def login(request):
    username = request.POST['username']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('/')
    else:
        return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class FeaturesViewSet(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

