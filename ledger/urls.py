from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/list', views.recipes_list, name='recipes_list'),
    path('recipe/1', views.recipe1, name='recipe1'),
    path('recipe/2', views.recipe2, name='recipe2')
]

app_name = 'ledger'