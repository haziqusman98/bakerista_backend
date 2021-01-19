from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import inventory_list, inventory_item, addOrder, addOrderDetail

urlpatterns = [
    path('inventory', inventory_list.as_view()),
    path('inventory/', inventory_item.as_view()),
    path('order/', addOrder.as_view()),
    path('orderdetail/', addOrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
