from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.JSONField()  # Store list of ingredients
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey to Category model
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cooking_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.title


