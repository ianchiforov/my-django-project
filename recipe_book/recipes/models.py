from django.db import models
from django.utils.text import slugify
from django.db.models import signals
from django.dispatch import receiver
from datetime import time


# Create your models here.
class Recipe:
    name = models.CharField(max_length=120)
    time_to_cook = models.TimeField(default=time(1))
    complexity = models.IntegerField()
    calories = models.IntegerField()
    recipe_text = models.TextField()


@receiver(signals.pre_save, sender=Recipe)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
