import pytest
from rest_framework.test import APIClient
from django.urls import reverse

def test_create_patient():
client = APIClient()
url = reverse('patient-list')
data = {
"name": "John Doe",
"age": 30,
"email": "john@test.com"
}

response = client.post(url, data, format='json')

assert response.status_code == 201
