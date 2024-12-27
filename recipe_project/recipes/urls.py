from django.urls import path
from .views import (
    RecipeListByCategoryView,             
    RecipeListByIngredientView,           
    RecipeListByMultipleIngredientsView,  
    RecipeListCreateView,                 
    RecipeDetailView,                    
    UserCreateView                     
)

urlpatterns = [
    
    path('recipes/category/<str:category_name>/', RecipeListByCategoryView.as_view(), name='recipe-by-category'),
    
    
    path('recipes/ingredient/<str:ingredient_name>/', RecipeListByIngredientView.as_view(), name='recipe-by-ingredient'),
    
    
    path('recipes/ingredients/', RecipeListByMultipleIngredientsView.as_view(), name='recipe-by-multiple-ingredients'),
    
    
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    
    
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    
    
    path('users/create/', UserCreateView.as_view(), name='user-create'),
]

