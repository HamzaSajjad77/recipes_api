from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions',
            'category', 'area', 'image_url', 'video_url', 'source_url', 'created_at'
        ]