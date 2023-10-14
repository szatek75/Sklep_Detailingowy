import paypalrestsdk
from django.shortcuts import render, get_object_or_404, redirect
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Order, Product, Category, Cart, CartItem, OrderItem
from .forms import UserProfileForm, PayPalPaymentForm, CheckoutForm
from django.http import HttpResponse


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.order_items.all()

    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'detailingstore/order_detail.html', context)

def home(request):
    return render(request, 'detailingstore/home.html')

def product_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'detailingstore/product_list.html', {'products': products, 'categories': categories})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'detailingstore/order_list.html', {'orders': orders})


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
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            if first_name and last_name:
                user_profile.first_name = first_name
                user_profile.last_name = last_name

            user_profile.address = form.cleaned_data.get('address')
            user_profile.save()

            return redirect('profile_view')

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'detailingstore/edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    user_profile = user.userprofile

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


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    return render(request, 'detailingstore/cart.html', {'cart': cart, 'cart_items': cart_items})


@login_required
def create_order(request):
    user_cart = get_object_or_404(Cart, user=request.user)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['shipping_address']

            total_amount = sum(item.product.price * item.quantity for item in user_cart.cartitem_set.all())

            user_orders_count = Order.objects.filter(user=request.user).count()
            order_number = f"Order-{user_orders_count + 1}"

            new_order = Order(
                user=request.user,
                cart=user_cart,
                order_number=order_number,
                total_amount=total_amount,
                shipping_address=address,
            )
            new_order.save()

            user_cart.cartitem_set.all().delete()

            return redirect('payment')
    else:
        form = CheckoutForm()

    return render(request, 'detailingstore/create_order.html', {'form': form, 'user_cart': user_cart})


@login_required
def payment(request):
    return render(request, 'detailingstore/payment.html')

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
            cart_item.delete()
        else:
            cart_item.quantity = new_quantity
            cart_item.save()

    return render(request, 'detailingstore/cart.html', {'cart': user_cart, 'cart_items': cart_items})


@login_required
def add_to_cart(request, product_id):
    quantity = request.GET.get('quantity', 1)
    product = get_object_or_404(Product, pk=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)

    if user_cart.products.filter(id=product_id).exists():
        cart_item = CartItem.objects.get(cart=user_cart, product=product)
        cart_item.quantity += int(quantity)
        cart_item.save()
    else:
        cart_item = CartItem(cart=user_cart, product=product, quantity=int(quantity))
        cart_item.save()

    return redirect('product_list')

def create_payment(request):
    if request.method == 'POST':
        form = PayPalPaymentForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.render())
    else:
        form = PayPalPaymentForm()
    return render(request, 'detailingstore/payment_form.html', {'form': form})

def paypal_ipn(request):
    return HttpResponse("OK")

def payment_success(request):
    return render(request, 'detailingstore/success.html')

def payment_cancel(request):
    return render(request, 'detailingstore/cancel.html')


