from rest_framework import generics, permissions
from .models import Recipe
from .serializers import RecipeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

