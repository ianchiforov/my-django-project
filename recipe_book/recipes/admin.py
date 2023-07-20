from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, Measure, IngredientMeasure

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measure)
admin.site.register(IngredientMeasure)
