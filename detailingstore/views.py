from django.shortcuts import render, get_object_or_404, redirect
from detailingstore.models import Category, ProductImage, OrderStatus, ShippingAddress, PaymentMethod, Product, Customer, Order
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Order, Product, Category, Cart, CartItem, OrderItem
from .forms import UserProfileForm, AddToCartForm, CartItemForm


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
    category_id = request.GET.get('category')
    categories = Category.objects.all()  # Pobierz dostępne kategorie

    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'detailingstore/product_list.html', {'products': products, 'categories': categories})

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


def products_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)

    return render(request, 'detailingstore/products_by_category.html', {'category': category, 'products': products})

# def add_to_cart(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     if request.method == 'POST':
#         form = AddToCartForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             cart, created = Cart.objects.get_or_create(user=request.user)
#             cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#             cart_item.quantity += quantity
#             cart_item.save()
#             return redirect('cart')
#     else:
#         form = AddToCartForm()
#     return render(request, 'detailingstore/add_to_cart.html', {'form': form})

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'detailingstore/cart.html', {'cart': cart, 'cart_items': cart_items})

def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        # Tworzenie zamówienia
        order = Order(user=request.user)
        order.save()

        # Dodawanie produktów z koszyka do zamówienia
        for item in cart.cartitem_set.all():
            order_item = OrderItem(order=order, product=item.product, quantity=item.quantity)
            order_item.save()

        # Czyszczenie koszyka
        cart.cartitem_set.all().delete()

        return redirect('order_confirmation', order_id=order.id)

    return render(request, 'detailingstore/checkout.html', {'cart': cart})

@login_required
def order_history(request):
    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'detailingstore/order_history.html', {'orders': user_orders})

@login_required
def cart(request):
    try:
        user_cart = Cart.objects.get(user=request.user)
        cart_items = user_cart.cartitem_set.all()
    except Cart.DoesNotExist:
        user_cart = None
        cart_items = []

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_quantity = int(request.POST.get('quantity'))

        cart_item = get_object_or_404(CartItem, cart=user_cart, product__id=product_id)

        if new_quantity == 0:
            # Jeśli nowa ilość wynosi 0, usuń produkt z koszyka
            cart_item.delete()
        else:
            cart_item.quantity = new_quantity
            cart_item.save()

    return render(request, 'detailingstore/cart.html', {'cart': user_cart, 'cart_items': cart_items})


@login_required
def add_to_cart(request, product_id):
    quantity = request.GET.get('quantity', 1)  # Domyślnie 1, ale można zmienić na wartość przekazywaną z formularza
    product = get_object_or_404(Product, pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)

    # Sprawdź, czy produkt już istnieje w koszyku
    if user_cart.products.filter(id=product_id).exists():
        # Jeśli istnieje, zaktualizuj ilość
        cart_item = CartItem.objects.get(cart=user_cart, product=product)
        cart_item.quantity += int(quantity)
        cart_item.save()
    else:
        # Jeśli nie istnieje, dodaj nowy element do koszyka
        cart_item = CartItem(cart=user_cart, product=product, quantity=int(quantity))
        cart_item.save()

    return redirect('product_list')

def checkout(request):
    return render(request, 'detailingstore/checkout.html')