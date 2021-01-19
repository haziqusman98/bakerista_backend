import uuid
from django.db import models


class Inventory(models.Model):
    item_code = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=500)
    image = models.URLField()
    quantity = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return f'Item: {self.name} - Price:{self.price}'


class Order(models.Model):
    order_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=100)
    customer_city = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=1000)
    customer_email = models.EmailField(max_length=500)
    customer_phone = models.CharField(max_length=20)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateField()

    def __str__(self):
        return f'Order: {self.order_number} - Date: {self.order_date}'


class OrderDetail(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    item_code = models.UUIDField()
    item_quantity = models.PositiveIntegerField()
    item_price = models.PositiveIntegerField(null=False, default=None)

    def __str__(self):
        return f'Order: {self.order_number} - Name: {self.item_name} - Quantity: {self.item_quantity}'
