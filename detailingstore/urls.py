from django.urls import path
from . import views

urlpatterns = [
    # URL-e dla widoków kategorii
    path('categories/', views.category_list_view, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail_view, name='category_detail'),

    # URL-e dla widoków zdjęć produktów
    path('product-images/', views.product_image_list_view, name='product_image_list'),
    path('product-images/<int:image_id>/', views.product_image_detail_view, name='product_image_detail'),

    # URL-e dla widoków statusów zamówienia
    path('order-statuses/', views.order_status_list_view, name='order_status_list'),
    path('order-statuses/<int:status_id>/', views.order_status_detail_view, name='order_status_detail'),

    # URL-e dla widoków adresów dostawy
    path('shipping-addresses/', views.shipping_address_list_view, name='shipping_address_list'),
    path('shipping-addresses/<int:address_id>/', views.shipping_address_detail_view, name='shipping_address_detail'),

    # URL-e dla widoków metod płatności
    path('payment-methods/', views.payment_method_list_view, name='payment_method_list'),
    path('payment-methods/<int:method_id>/', views.payment_method_detail_view, name='payment_method_detail'),

    # URL-e dla widoków produktów
    # path('products/', views.product_list_view, name='product_list'),
    # path('products/<int:product_id>/', views.product_detail_view, name='product_detail'),

    # URL-e dla widoków klientów
    path('customers/', views.customer_list_view, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail_view, name='customer_detail'),

    # URL-e dla widoków zamówień
    # path('orders/', views.order_list_view, name='order_list'),
    # path('orders/<int:order_id>/', views.order_detail_view, name='order_detail'),

    # URL dla strony głównej
    path('', views.home, name='home'),

    path('products/', views.product_list, name='product_list'),

    path('orders/', views.order_list, name='order_list'),

    path('promotions/', views.promotions, name='promotions'),

    path('contact/', views.contact, name='contact'),
]