from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from PIL import Image
import numpy as np
import random
import string
import re


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    is_business = models.BooleanField("owner", default=False)

    def __str__(self):
        return self.email


def code_registration(length=6):
    code = "string.ascii_letters + string.digits"
    return "".join(random.choice(code) for i in range(length))


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE,)
    location = models.CharField(verbose_name="profile", max_length=30,)
    favorites = models.ManyToManyField(
        verbose_name="user_favorites", default="No Favorites Yet!"
    )
    email_regex = RegexValidator(
        regex=r"^[a-z0-9\._]+@\w+\.\w{2,3}$",
        flags=re.IGNORECASE,
        message="Email Address must be entered for verification",
    )
    email = models.EmailField(
        verbose_name="user_email", validators=[email_regex], blank=True,
    )
    registration = models.CharField(
        verbose_name="registration_code", max_length=15, default=code_registration,
    )
    links = models.URLField(verbose_name="shared_links", blank=True,)
    image = models.ImageField(blank=True)


class Location(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="location", null=True,
    )
    email_regex = RegexValidator(
        regex=r"^[a-z0-9\._]+@\w+\.\w{2,3}$",
        flags=re.IGNORECASE,
        message="Email Address must be entered for verification",
    )
    email = models.EmailField(
        verbose_name="location_email", validators=[email_regex], blank=True,
    )
    name = models.CharField(verbose_name="location_name", max_length=100,)
    address = models.CharField(verbose_name="location_address", max_length=50,)
    city = models.CharField(verbose_name="location_city", max_length=50,)
    # state=models.CharField(verbose_name='location_state', max_length=2,)ADD DROP DOWN MENU
    zipcode = models.CharField(verbose_name="location_zip", max_length=10,)
    website = models.URLField(verbose_name="location_website", blank=True,)
    phone = models.CharField(verbose_name="location_phone", max_length=10,)
    biz_open = models.TimeField(verbose_name="location_open", max_length=50)
    biz_close = models.TimeField(verbose_name="location_close", max_length=50)
    # (Is there a way to make business hours a multiple entry field?)
    res_join = models.DateTimeField(verbose_name="date_res_join", auto_now_add=True,)
    res_mod = models.DateTimeField(verbose_name="date_res_mod", auto_now=True,)
    res_image = models.ImageField(verbose_name="restaurant_image", blank=True,)


class Features(models.Model):
    offered = models.CharField(max_length=50)
    description = models.TextField()
    ##How do I set the ratings properly?
    feat_rating = models.IntegerField(
        verbose_name="feature_rating",
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )


class Reviews(models.Model):
    overall = models.IntegerField(
        verbose_name="main_rating",
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )
    # def average_rating(self):
    #     all_ratings = map(lambda x: x.rating, self.review_set.all())
    #     return np.mean(all_ratings)

    # def __unicode__(self):
    #     return self.name
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    feature = models.ForeignKey("Features", on_delete=models.CASCADE)
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        related_name="reviews",
        on_delete=models.CASCADE,
    )


class Comments(models.Model):
    user = models.ForeignKey(
        User, related_name="user_comments", on_delete=models.SET_NULL, null=True,
    )
    review = models.ForeignKey(
        Reviews, related_name="user_comments", on_delete=models.CASCADE,
    )
    content = models.TextField(verbose_name="review_comment",)
    com_create = models.DateTimeField(
        verbose_name="date_comment_created", auto_now_add=True
    )
    com_mod = models.DateTimeField(verbose_name="date_comment_modified", auto_now=True)


class Category(models.Model):
    name = models.CharField(verbose_name="category_name", max_length=10, unique=True,)

    def __str__(self):
        return self.name


class Favorites(models.Model):
    user = models.ForeignKey(
        User, related_name="favorite_places", on_delete=models.SET_NULL, null=True,
    )
