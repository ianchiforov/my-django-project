from django.shortcuts import render
from recipes.models import Recipe


# Create your views here.
def welcome(request):
    return render(request, "main_website/welcome.html",
                  {
                      "recipes": Recipe.objects.all()
                  })
