from django.db import models
from django.utils.text import slugify
from django.db.models import signals
from django.dispatch import receiver
from datetime import time
from autoslug import AutoSlugField


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    time_to_cook = models.IntegerField()
    complexity = models.IntegerField()
    calories = models.IntegerField()
    recipe_text = models.TextField()
    slug = AutoSlugField(populate_from='name',
                         primary_key=True,
                         unique=True,
                         )

    def __str__(self):
        return f"""{self.name} ({self.slug})
        time to cook: {self.time_to_cook} minutes
        complexity: {self.complexity} stars (out of 5)
        calories: {self.calories}
        recipe text: {self.recipe_text}"""


# @receiver(signals.pre_save, sender=Recipe)
# def populate_slug(sender, instance, **kwargs):
#     instance.slug = slugify(instance.name)
