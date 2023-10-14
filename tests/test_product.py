import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from detailingstore.models import Product, Category


@pytest.mark.django_db
def test_create_and_retrieve_product():
    # Tworzenie kategorii
    category = Category.objects.create(name='Test Category')

    # Tworzenie produktu
    product = Product.objects.create(
        name='Test Product',
        description='Description for the test product',
        price=10,
        category=category,
        stock=100
    )

    assert Product.objects.count() == 1

    retrieved_product = Product.objects.get(name='Test Product')
    assert retrieved_product.name == 'Test Product'
    assert retrieved_product.description == 'Description for the test product'
    assert retrieved_product.price == 10
    assert retrieved_product.category == category
    assert retrieved_product.stock == 100

    # Testowanie pola image
    image = SimpleUploadedFile("product.jpg", b"file_content", content_type="image/jpg")
    retrieved_product.image = image
    retrieved_product.save()
    assert 'products/' in retrieved_product.image.url

