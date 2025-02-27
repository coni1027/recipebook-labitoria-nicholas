from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.

def index(request):
    return HttpResponse("Landing page")


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(DetailView):
    model = models.Recipe
    template_name = 'recipe_view.html'