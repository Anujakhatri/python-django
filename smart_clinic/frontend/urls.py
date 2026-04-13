from django.contrib.auth import login
from django.urls import path
from .views import home, login_page, register_page

urlpatterns = [
    path('', home),
    path('login/', login_page),
    path('register/', register_page),
]