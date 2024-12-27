from recipes.models import Recipe, Category, User

def seed_data():
    # Fetch the Dessert category
    category, _ = Category.objects.get_or_create(name='Dessert')

    # Fetch or create a user
    user, _ = User.objects.get_or_create(username='testuser', email='test@example.com')
    user.set_password('testpass')
    user.save()

    # Create a recipe
    Recipe.objects.create(
        title='Chocolate Cake',
        description='Rich and moist chocolate cake.',
        ingredients='["flour", "sugar", "cocoa powder", "eggs", "milk"]',
        instructions='Mix all ingredients and bake for 30 minutes at 180°C.',
        category=category,
        preparation_time=20,
        cooking_time=30,
        servings=8,
        user=user
    )
    print("Seed data added successfully.")
