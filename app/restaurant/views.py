from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponseRedirect

from .models import Category,FoodItem


class CategoryListView(ListView):
    model = Category
    ordering = "name"
    template_name = "category_list.html"
    paginate_by = 2

class CategoryDetailView(ListView):
    model = Category
    ordering = "name"
    template_name = "category_detail.html"
    paginate_by = 2


class FoodItemListView(ListView):
    model = FoodItem
    ordering = "name"
    template_name = "fooditem_list.html"
    paginate_by = 2

    def get_ordering(self):
        order_by = self.request.GET.get("order_by")

        if not order_by:
            return self.ordering

        if hasattr(self.model, order_by.removeprefix("-")):
            return order_by

        return self.ordering


class FoodItemDetailView(DetailView):
    model = FoodItem
    template_name = "fooditem_detail.html"



