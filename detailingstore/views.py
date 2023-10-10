from django.shortcuts import render, get_object_or_404
from detailingstore.models import Category, ProductImage, OrderStatus, ShippingAddress, PaymentMethod, Product, Customer, Order

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'detailingstore/category_list.html', {'categories': categories})

def category_detail_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'detailingstore/category_detail.html', {'category': category})

def product_image_list_view(request):
    images = ProductImage.objects.all()
    return render(request, 'detailingstore/product_image_list.html', {'images': images})

def product_image_detail_view(request, image_id):
    image = get_object_or_404(ProductImage, pk=image_id)
    return render(request, 'detailingstore/product_image_detail.html', {'image': image})

def order_status_list_view(request):
    statuses = OrderStatus.objects.all()
    return render(request, 'detailingstore/order_status_list.html', {'statuses': statuses})

def order_status_detail_view(request, status_id):
    status = get_object_or_404(OrderStatus, pk=status_id)
    return render(request, 'detailingstore/order_status_detail.html', {'status': status})

def shipping_address_list_view(request):
    addresses = ShippingAddress.objects.all()
    return render(request, 'detailingstore/shipping_address_list.html', {'addresses': addresses})

def shipping_address_detail_view(request, address_id):
    address = get_object_or_404(ShippingAddress, pk=address_id)
    return render(request, 'detailingstore/shipping_address_detail.html', {'address': address})

def payment_method_list_view(request):
    methods = PaymentMethod.objects.all()
    return render(request, 'detailingstore/payment_method_list.html', {'methods': methods})

def payment_method_detail_view(request, method_id):
    method = get_object_or_404(PaymentMethod, pk=method_id)
    return render(request, 'detailingstore/payment_method_detail.html', {'method': method})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'detailingstore/product_list.html', {'products': products})

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detailingstore/product_detail.html', {'product': product})

def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request, 'detailingstore/customer_list.html', {'customers': customers})

def customer_detail_view(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'detailingstore/customer_detail.html', {'customer': customer})

def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'detailingstore/order_list.html', {'orders': orders})

def order_detail_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'detailingstore/order_detail.html', {'order': order})

def home(request):
    return render(request, 'detailingstore/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'detailingstore/products.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'detailingstore/orders.html', {'orders': orders})

def promotions(request):
    return render(request, 'detailingstore/promotions.html')

def contact(request):
    return render(request, 'detailingstore/contact.html')