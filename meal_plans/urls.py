from django.urls import path
from meal_plans.views import (
    MealPlanListView,
    MealPlanCreateView,
    MealPlanUpdateView,
    MealPlanDetailView,
    MealPlanDeleteView,
)

urlpatterns = [
    path("", MealPlanListView.as_view(), name="meal_plan_list"),
    path("<int:pk>/", MealPlanDetailView.as_view(), name="meal_plans_detail"),
    path(
        "<int:pk>/delete/",
        MealPlanDeleteView.as_view(),
        name="meal_plans_delete",
    ),
    path("new/", MealPlanCreateView.as_view(), name="meal_plans_new"),
    path(
        "<int:pk>/edit/", MealPlanUpdateView.as_view(), name="meal_plans_edit"
    ),
    # path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
