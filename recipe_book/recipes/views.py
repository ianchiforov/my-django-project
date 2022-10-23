from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm


# Create your views here.
def detail(request, slug):
    recipe = get_object_or_404(Recipe, pk=slug)
    return render(request, "recipes/detail.html",
                  {
                      "recipe": recipe
                  })


def new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = RecipeForm()
    return render(request, "recipes/new.html",
                  {
                      "form": form
                  })
