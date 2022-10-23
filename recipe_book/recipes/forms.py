from .models import Recipe
from django.forms import ModelForm, TextInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {
            "time_to_cook": TextInput(attrs={
                "type": "number",
                "min": 1,
                "max": 999
            }),
            "complexity": TextInput(attrs={
                "type": "number",
                "min": 1,
                "max": 5
            }),
            "calories": TextInput(attrs={
                "type": "number",
                "min": 1,
                "max": 9999
            })
        }
