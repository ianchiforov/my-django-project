from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm
from django.core.paginator import Paginator


# Create your views here.
def detail(request, slug):
    print(999)
    recipe = get_object_or_404(Recipe, slug=slug)
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


def recipes(request):
    recipes_list = Recipe.objects.all()
    paginator = Paginator(recipes_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "recipes/recipes.html",
                  {
                      "page_obj": page_obj
                  })
