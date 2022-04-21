from django.contrib import admin


# Register your models here.
from .models import Receipe, Measure, FoodItem, Ingredients, Step


class ReceipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipe, ReceipeAdmin)


class MeasureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Measure, MeasureAdmin)


class FoodItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(FoodItem, FoodItemAdmin)


class IngredientsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredients, IngredientsAdmin)


class StepAdmin(admin.ModelAdmin):
    pass


admin.site.register(Step, StepAdmin)
