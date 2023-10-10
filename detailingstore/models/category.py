from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Inne pola, takie jak obrazek kategorii, itp.

    def __str__(self):
        return self.name
