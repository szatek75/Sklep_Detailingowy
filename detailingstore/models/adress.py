from django.db import models
from detailingstore.models.customer import Customer


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"Adres dostawy dla {self.customer.first_name} {self.customer.last_name}"
