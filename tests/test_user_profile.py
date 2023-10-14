import pytest
from django.contrib.auth.models import User
from detailingstore.models import UserProfile

@pytest.mark.django_db
def test_create_user_profile():
    user = User.objects.create_user(username='testuser', password='testpassword')
    profile = UserProfile.objects.get(user=user)
    assert profile is not None

@pytest.mark.django_db
def test_user_profile_fields():
    user = User.objects.create_user(username='testuser', password='testpassword')
    profile = UserProfile.objects.get(user=user)
    assert profile.first_name == ""
    assert profile.last_name == ""

@pytest.mark.django_db
def test_update_user_profile():
    user = User.objects.create_user(username='testuser', password='testpassword')
    profile = UserProfile.objects.get(user=user)
    profile.first_name = "John"
    profile.last_name = "Doe"
    profile.save()
    updated_profile = UserProfile.objects.get(user=user)
    assert updated_profile.first_name == "John"
    assert updated_profile.last_name == "Doe"
