from rest_framework import serializers
from .models import Recipe, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    ingredients = serializers.ListField(
        child=serializers.CharField(max_length=255)  # Each ingredient as a string
    )

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user  # Get the authenticated user
        validated_data['user'] = user  # Assign the authenticated user to the recipe
        return super().create(validated_data)
