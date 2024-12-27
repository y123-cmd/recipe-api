from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Recipe, Category, Ingredient
from .serializers import RecipeSerializer
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from django.http import JsonResponse

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'email']  # Add or remove fields as needed
    template_name = 'user_form.html'  # Specify the template for this view
    success_url = reverse_lazy('login')  # Redirect to login page upon successful user creation

class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# List recipes filtered by category
class RecipeListByCategoryView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        try:
            category = Category.objects.get(name=category_name)
            return Recipe.objects.filter(category=category)
        except Category.DoesNotExist:
            return Recipe.objects.none()  # Return an empty queryset if category does not exist

# List recipes filtered by a single ingredient
class RecipeListByIngredientView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        ingredient_name = self.kwargs.get('ingredient_name')
        return Recipe.objects.filter(ingredients__name__icontains=ingredient_name)

# List recipes filtered by multiple ingredients
class RecipeListByMultipleIngredientsView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        ingredient_names = self.request.query_params.getlist('ingredients')
        query = Q()
        for ingredient in ingredient_names:
            query &= Q(ingredients__name__icontains=ingredient)
        return Recipe.objects.filter(query)

# Retrieve recipes containing a specific ingredient
@api_view(['GET'])
def recipes_by_ingredient(request, ingredient):
    """
    Retrieve recipes containing a specific ingredient.
    """
    recipes = Recipe.objects.filter(ingredients__icontains=ingredient)
    if recipes.exists():
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=200)
    return Response({"message": f"No recipes found containing '{ingredient}'"}, status=404)
# Function-based view for listing recipes by multiple ingredients
def recipes_by_multiple_ingredients(request):
    # Example logic for the view
    if request.method == "GET":
        # You can handle the logic for fetching recipes by multiple ingredients here
        data = {"message": "Recipes by multiple ingredients will be listed here."}
        return JsonResponse(data)
    return JsonResponse({"error": "Invalid request method"}, status=405)
