from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from psycopg2 import IntegrityError

from recipes.forms import RatingForm

# from recipes.forms import RecipeForm
from recipes.models import FoodItem, Ingredient, Recipe, ShoppingItem


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        try:
            if form.is_valid():
                rating = form.save(commit=False)
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
        except Recipe.DoesNotExist:
            return redirect("recipes_list")
    return redirect("recipe_detail", pk=recipe_id)


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 4


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        # COME BACK TO UNDERSTAND FOR LOOP HERE
        # COME BACK TO UNDERSTAND FOR LOOP HERE
        # COME BACK TO UNDERSTAND FOR LOOP HERE
        # COME BACK TO UNDERSTAND FOR LOOP HERE
        # COME BACK TO UNDERSTAND FOR LOOP HERE
        # COME BACK TO UNDERSTAND FOR LOOP HERE
        # shoppingitem refers to class ShoppingItem from Models Y THO
        foods = []
        for item in self.request.user.shoppingitem.all():
            foods.append(item.food_item)
        context["servings"] = self.request.GET.get("servings")
        context["food_in_shopping_list"] = foods
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image", "servings"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "description", "image", "servings"]
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")


class ShoppingListView(LoginRequiredMixin, ListView):
    model = ShoppingItem
    template_name = "recipes/shopping_items/list.html"


# not necessary - do not need create form for this function because list is returned from listview // items are added based off of recipes
# class ShoppingListCreateView(LoginRequiredMixin, CreateView):
#     model = ShoppingItem
#     template_name = "recipes/shopping_items/create.html"
# success_url = reverse_lazy("shopping_items_list")


def create_shopping_item(request):
    ingredient_id = request.POST.get("ingredient_id")
    ingredient = Ingredient.objects.get(id=ingredient_id)
    user = request.user
    try:
        ShoppingItem.objects.create(
            food_item=ingredient.food,
            user=user,
        )
    except IntegrityError:
        pass
    return redirect("recipe_detail", pk=ingredient.recipe.id)


# class ShoppingListDeleteView(LoginRequiredMixin, DeleteView):
#     model = ShoppingItem
#     template_name = "recipes/shopping_items/delete.html"
#     success_url = reverse_lazy("shopping_items_list")


def delete_all_shopping_items(request):
    ShoppingItem.objects.filter(user=request.user).delete()
    return redirect("shopping_item_list")
