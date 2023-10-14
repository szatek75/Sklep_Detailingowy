from django.urls import path
from allauth.account.views import SignupView, LoginView, LogoutView, PasswordResetView, ConfirmEmailView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import cart, payment_success, payment_cancel, order_list, order_detail, confirm_email

urlpatterns = [
    path('', views.home, name='home'),

    path('products/', views.product_list, name='product_list'),

    path('contact/', views.contact, name='contact'),

    path('accounts/login/', LoginView.as_view(template_name='detailingstore/login.html'), name='account_login'),
    path('accounts/signup/', SignupView.as_view(template_name='detailingstore/signup.html'), name='account_signup'),
    path('accounts/password/reset/', PasswordResetView.as_view(template_name='detailingstore/password_reset.html'),
         name='account_reset_password'),
    path('accounts/confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),

    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),

    path('profil/', views.edit_profile, name='edit_profile'),

    path('profil/wyswietl/', views.profile_view, name='profile_view'),

    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),

    path('cart/', cart, name='cart'),

    path('product/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),

    path('payment-success/', payment_success, name='payment_success'),
    path('payment-cancel/', payment_cancel, name='payment_cancel'),

    path('orders/', order_list, name='order_list'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),

    path('create_order/', views.create_order, name='create_order'),

    path('payment/', views.payment, name='payment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)