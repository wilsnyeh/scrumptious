from pyexpat import model
from django.db import models


# Create your models here.
class Receipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " created by " + self.author


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name + " (" + self.abbreviation + ")"


class FoodItem(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        pass


class Ingredients(models.Model):
    amount = models.FloatField()
    receipe = models.ForeignKey(
        Receipe, related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey(Measure, on_delete=models.PROTECT)
    food = models.ForeignKey(FoodItem, on_delete=models.PROTECT)

    def __str__(self):
        pass


class Step(models.Model):
    receipe = models.ForeignKey(
        Receipe, related_name="steps", on_delete=models.CASCADE
    )
    order = models.SmallIntegerField()
    directions = models.CharField(max_length=300)

    def __str__(self):
        pass
