from django.contrib.auth import login
from django.urls import path
from .views import home, login_page, register_page, doctor_home, patient_home

app_name = 'frontend'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('doctor_home/', doctor_home, name='doctor_home'),
    path('patient_home/', patient_home, name='patient_home')
]