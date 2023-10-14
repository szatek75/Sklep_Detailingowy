from django.db import models
from django.contrib.auth.models import User
from .product import Product
from .cart import Cart
from django.utils import timezone
from djmoney.models.fields import MoneyField
from djmoney.money import Money

# Model zamówienia
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    order_number = models.CharField(max_length=255, default="")
    order_name = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField(default=timezone.now)
    shipping_address = models.CharField(max_length=100)
    total_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='PLN', default=Money(0, 'PLN'))
    order_items = models.ManyToManyField('OrderItem')

    def __str__(self):
        return self.order_number

# Model produktów w zamówieniu
class OrderItem(models.Model):
    order_reference = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
#
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super().save(*args, **kwargs)