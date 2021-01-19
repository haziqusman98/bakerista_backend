from rest_framework import serializers
from .models import Order, Inventory, OrderDetail


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['item_code', 'name', 'price',
                  'description', 'image', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_number', 'customer_name', 'customer_city', 'customer_address',
                  'customer_email', 'customer_phone', 'order_date', 'delivery_date']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['order_number', 'item_name',
                  'item_code', 'item_price', 'item_quantity']
