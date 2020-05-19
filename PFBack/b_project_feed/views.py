from django.shortcuts import render
from django.http import HttpResponse
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


