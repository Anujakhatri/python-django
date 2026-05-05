import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from clinic_project.clinic.models import Doctor

@pytest.mark.django_db
def test_get_doctor_list():

    Doctor.objects.create(
        name="Dr. Smith",
        specialization="Cardiology",
        experience="10 years"
    )

    client = APIClient()

    url = reverse('doctor-list')

    response = client.get(url)

    assert response.status_code == 200

    assert len(response.data) == 1
    assert response.data[0]['name'] == "Dr. Smith"
