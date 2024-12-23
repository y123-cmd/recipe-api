from django.urls import path
from .views import UserCreateView, RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]
