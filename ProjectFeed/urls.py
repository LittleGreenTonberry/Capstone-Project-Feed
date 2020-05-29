from django.urls import include,path
from django.views.generic import TemplateView
from rest_framework import routers
from .views import LocationViewSet, FeaturesViewSet,ProfileViewSet,ReviewsViewSet,CommentsViewSet,CategoryViewSet
from . import views
app_name="ProjectFeed"
router = routers.DefaultRouter()
router.register(r"locations", LocationViewSet, basename='locations')
router.register(r"features", FeaturesViewSet, basename='features')
router.register(r"profile", ProfileViewSet, basename='profile')
router.register(r"reviews", ReviewsViewSet, basename='reviews')
router.register(r"comments", CommentsViewSet, basename='comments')
router.register(r"category", CategoryViewSet, basename='category')
urlpatterns=router.urls
urlpatterns = [
    path("",include(router.urls)),
    
    
]
