from django.contrib import admin
from .models import Product, Customer, Order, Category, ProductImage, OrderStatus, ShippingAddress, PaymentMethod

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(OrderStatus)
admin.site.register(ShippingAddress)
admin.site.register(PaymentMethod)
