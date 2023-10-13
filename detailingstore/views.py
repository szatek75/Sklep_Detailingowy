from django.shortcuts import render, get_object_or_404, redirect
from detailingstore.models import Category, ProductImage, OrderStatus, ShippingAddress, PaymentMethod, Product, Customer, Order
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Order, Product
from .forms import UserProfileForm


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

def product_list(request):
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

class MyLoginView(LoginView):
    template_name = 'detailingstore/login.html'

@login_required
def user_orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'detailingstore/order_list.html', {'orders': orders})

@login_required
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)

        if form.is_valid():
            # Ustal, czy dane "imię" i "nazwisko" są dostępne
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            if first_name and last_name:
                # Jeśli dostarczono dane "imię" i "nazwisko", zapisz je do profilu
                user_profile.first_name = first_name
                user_profile.last_name = last_name

            # Zapisz inne dane profilu
            user_profile.address = form.cleaned_data.get('address')
            user_profile.save()

            return redirect('profile_view')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'detailingstore/edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    # Tutaj możesz dodać kod do pobrania danych użytkownika i przekazania ich do szablonu.
    user = request.user
    user_profile = user.userprofile  # Zakłada, że masz model UserProfile z polem 'user' jako OneToOneField

    context = {
        'user': user,
        'user_profile': user_profile,
    }

    return render(request, 'detailingstore/profile.html', context)

@login_required
def profile(request):
    user = request.user
    return render(request, 'detailingstore/profile.html', {'user': user})