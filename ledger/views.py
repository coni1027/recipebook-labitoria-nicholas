from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.

def index(request):
    return HttpResponse("Landing page")

def recipes_list(request):
    recipes_list = models.Recipe.objects.all()
    ctx = {"recipe" : recipes_list}

    return render(request, "ledger/recipes_list.html", ctx)

def recipe(request, pk):
    recipe = models.Recipe.objects.get(pk=pk)
    ctx = {"recipe" : recipe}

    return render(request, "ledger/recipes_view.html", ctx)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'ledger/recipes_view.html'