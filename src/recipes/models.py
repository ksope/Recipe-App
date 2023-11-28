from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=50)
    ingredients=models.CharField(max_length=255)
    cooking_time=models.PositiveIntegerField(help_text= 'in minutes')
    

    def __str__(self): 
        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"

        )
    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(', ')) < 4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients.split(', ')) >= 4:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients.split(', ')) < 4:
            self.difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(self.ingredients.split(', ')) >= 4:
            self.difficulty = 'Hard'

