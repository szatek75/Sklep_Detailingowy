from django.db import models
from detailingstore.models.customer import Customer
from detailingstore.models.product import Product

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Inne pola modelu Order

    def __str__(self):
        return f"Zamówienie {self.pk} - {self.customer}"
