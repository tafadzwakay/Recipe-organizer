from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField(help_text= "Preparation time in minutes")
    image = models.ImageField( upload_to= "recipe_images/", blank = True, null = True )

