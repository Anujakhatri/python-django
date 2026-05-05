import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse

User = get_user_model()  # returns accounts.User, not auth.User


@pytest.mark.django_db
def test_create_patient():
    # Create a test user and authenticate the client
    user = User.objects.create_user(username='anuja', password='3456')
    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('patient-list')
    data = {
        "name": "John Doe",
        "age": 30,
        "contact": "1234567890",
        "reason": "Routine Checkup"
    }

    response = client.post(url, data, format='json')
    print(response.data)   # shows exact validation errors if it still fails

    assert response.status_code == 201
