from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from projectfeed_app.views import (
    LocationViewSet,
    FeaturesViewSet,
    ProfileViewSet,
    ReviewsViewSet,
    CommentsViewSet,
    CategoryViewSet,
)

router = routers.DefaultRouter()
router.register(r"locations", LocationViewSet)
router.register(r"features", FeaturesViewSet)
router.register(r"profile", ProfileViewSet)
router.register(r"reviews", ReviewsViewSet)
router.register(r"comments", CommentsViewSet)
router.register(r"category", CategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    url(r"^api-auth/", include("rest_framework.urls")),
]
