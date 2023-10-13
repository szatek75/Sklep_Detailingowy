from django import forms
from .models import UserProfile
from allauth.account.forms import LoginForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'address']

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    address = forms.CharField(max_length=100, required=False)

class CustomLoginForm(LoginForm):
    login = forms.CharField(max_length=254, label="Nazwa użytkownika lub e-mail")

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)

class CartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Ilość')
