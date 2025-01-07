from django.urls import path
from . import views
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
   #recipe by multiple ingridients (CBV)

    path('recipes/ingredients/', RecipeListByMultipleIngredientsView.as_view(), name='recipe-by-multiple-ingredients'),

   #Recipes by multiple ingridients (FBV)
    path('recipes/by-multiple-ingredients/', views.recipes_by_multiple_ingredients, name='recipes-by-multiple-ingredients-fbv'),

    path('create/', views.create_recipe, name='create_recipe'),
    path('list/', views.recipe_list, name='list'),
    path('users/delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('users/update/<int:id>/', views.update_recipe, name='update_recipe'),

]



