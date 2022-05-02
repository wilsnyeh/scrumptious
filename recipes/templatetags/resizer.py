from django import template
from django.core.validators import MaxValueValidator, MinValueValidator

register = template.Library()


def resize_to(ingredient, target):
    serving = ingredient.recipe.servings
    if int(target) > 0 and abs(serving):
        if serving is not None and target is not None:
            try:
                return (int(target) / serving) * (ingredient.amount)
            except ValueError:
                return
    return ingredient.amount


register.filter(resize_to)
