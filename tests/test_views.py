import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_list_view(client):
    response = client.get(reverse('product_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_order_list_view(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('order_list'))
    assert response.status_code == 200