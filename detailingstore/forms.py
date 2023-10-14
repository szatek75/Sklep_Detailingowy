from django import forms
from .models import UserProfile
from allauth.account.forms import LoginForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

class CustomLoginForm(LoginForm):
    login = forms.CharField(max_length=254, label="Nazwa użytkownika lub e-mail")

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)

class CartItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Ilość')

from django import forms

class PayPalPaymentForm(forms.Form):
    # Parametry płatności
    item_name = forms.CharField(max_length=200, widget=forms.HiddenInput())
    amount = forms.DecimalField(widget=forms.HiddenInput())
    currency_code = forms.CharField(widget=forms.HiddenInput(), initial="USD")

    def __init__(self, *args, **kwargs):
        super(PayPalPaymentForm, self).__init__(*args, **kwargs)

        # Inicjalizacja parametrów formularza, na przykład z nazwą produktu i ceną
        self.fields['item_name'].initial = "Product Name"
        self.fields['amount'].initial = 10.00

    def render(self):
        # Generowanie formularza HTML
        form_html = '<form action="https://www.sandbox.paypal.com/cgi-bin/webscr" method="post">'
        for field_name, field in self.fields.items():
            form_html += str(field)
        form_html += '<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif" name="submit" alt="PayPal - The safer, easier way to pay online.">'
        form_html += '</form>'
        return form_html

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=255, label="Adres dostawy")
