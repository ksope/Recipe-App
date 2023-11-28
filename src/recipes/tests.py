from django.test import TestCase

from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
       Recipe.objects.create(name='Jack Potatoes', ingredients='potatoes, oil, bacon, vegetables, butter', cooking_time='25')

    #test to see if the book’s name is initialized as expected
    def test_recipe_name(self):
       # Get a book object to test
       recipe = Recipe.objects.get(id=1)

       # Get the metadata for the 'name' field and use it to query its data
       field_label = recipe._meta.get_field('name').verbose_name

       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    #test to ensure that the length of the ingredients field is a maximum of 120
    def test_ingredients_max_length(self):
           # Get a book object to test
           recipe = Recipe.objects.get(id=1)

           # Get the metadata for the 'author_name' field and use it to query its max_length
           max_length = recipe._meta.get_field('ingredients').max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 255)

    #test to validate all fields
    def recipe_is_valid(self):
        recipe = Recipe.objects.get(id=1)
        self.assertTrue(recipe.is_valid())