from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html', {'recipes': recipes})

def add_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']
        prep_time = request.POST['prep_time']
        Recipe.objects.create(name=name, ingredients=ingredients, instructions=instructions, prep_time=prep_time)
        return HttpResponseRedirect(reverse("home"))

    return render(request, 'recipe/add_recipe.html', {
        'form': RecipeForm()
    })

def view_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, "recipe/view_recipe.html", { 'recipe': recipe})

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return HttpResponseRedirect(reverse("home"))

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)     
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        recipe.save()
        return redirect('home')

    else:
        form= RecipeForm(instance=recipe)
        return render(request, 'recipe/update_recipe.html', {'form': form})


