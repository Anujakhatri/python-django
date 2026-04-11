from django.urls import path

from .views import doctor_list, doctor_detail

urlpatterns=[
    path('doctors/', doctor_list),
    path('doctors/<int:pk>/', doctor_detail)
]