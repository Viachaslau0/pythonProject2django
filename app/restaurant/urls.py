from django.urls import path
from . import views

urlpatterns = [
    path('restaurant/category/', views.CategoryListView.as_view(), name='category_list'),
    path('restaurant/category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('fooditems/', views.FoodItemListView.as_view(), name='fooditem_list'),
    path('fooditems/<slug:slug>/', views.FoodItemDetailView.as_view(), name='fooditem_detail'),
]