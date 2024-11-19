from .models import Recipe
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets ={
            "name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'recipe name'}),
            "ingredients": forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ingredients'}),
            "instructions": forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Steps to make the Recipe'}),
            "prep_time": forms.NumberInput(attrs={"class":"form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

