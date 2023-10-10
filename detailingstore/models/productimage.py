from django.db import models
from detailingstore.models.product import Product


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    # Inne pola, takie jak opis, kolejność itp.

    def __str__(self):
        return f"Zdjęcie produktu {self.product.name}"
