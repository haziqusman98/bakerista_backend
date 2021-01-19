from django.contrib import admin
from .models import Inventory, Order, OrderDetail

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderDetail)
