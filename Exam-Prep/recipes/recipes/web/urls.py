from django.contrib import admin
from django.urls import path

from recipes.web.views import show_home, create_recipe, edit_recipe, delete_recipe, recipe_details

urlpatterns = (
    path('', show_home, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', recipe_details, name='recipe details'),
)
