from django.db import models
from django.contrib.auth.models import User  # Upewnij się, że importujesz użytkownika z modułu django.contrib.auth.models
from .product import Product  # Zakładam, że masz model produktu o nazwie 'Product'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(default='Nowe', max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(OrderItem)  # Zmiana na pole ManyToMany do modelu OrderItem

    # Możesz dodać inne pola, takie jak adres dostawy itp.
