from django.shortcuts import render
from django.shortcuts import redirect


from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from meal_plans.models import MealPlan


# Create your views here.
class MealPlanListView(ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"
    paginate_by = 4


class MealPlanDetailView(DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("meal_plans_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "recipe"]
    success_url = reverse_lazy("meal_plans_list")


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")
