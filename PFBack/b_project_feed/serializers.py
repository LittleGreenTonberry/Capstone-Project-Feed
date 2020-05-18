from rest_framework import serializers
from .models import Location, Features,Profile,Reviews,Comments,Category

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields='__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'