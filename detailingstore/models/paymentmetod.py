from django.db import models
from detailingstore.models.customer import Customer

class PaymentMethod(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    # Inne pola, takie jak typ karty, CVV itp.

    def __str__(self):
        return f"Metoda płatności dla {self.customer.first_name} {self.customer.last_name}"
