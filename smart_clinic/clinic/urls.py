from django.urls import path

from clinic_project.clinic_project.urls import urlpatterns
from .views import doctor_list

urlpatterns=[
    path('doctors/', doctor_list),
]