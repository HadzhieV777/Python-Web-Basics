from django.contrib import admin

from recipes.web.models import Recipe


@admin.register(Recipe)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')
