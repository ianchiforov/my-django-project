from django.db import models
# from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.utils.text import slugify
# from django.dispatch import receiver
# from django.db.models import signals
from autoslug import AutoSlugField
# import django.utils.translation
# from transliterate import translit
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

Profile = get_user_model()


class Measure(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IngredientMeasure(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} {self.measure}(s) of {self.ingredient}"


def custom_slugify(value):
    return "-".join(value.split())


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    time_to_cook = models.PositiveIntegerField(help_text='Time in minutes')
    complexity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    servings = models.PositiveSmallIntegerField(default=1)
    steps_to_cook = models.TextField()
    ingredients = models.ManyToManyField(IngredientMeasure)
    slug = AutoSlugField(populate_from="name", unique=True, slugify=custom_slugify)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=User.objects.first().pk)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    # def get_name(self):
    #     return self.name.encode()


# @receiver(signals.pre_save, sender=Recipe)
# def populate_slug(sender, instance, **kwargs):
#     instance.slug = slugify(instance.name)
