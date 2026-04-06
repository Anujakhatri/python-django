from django.urls import path
from . import views
from . import db

urlpatterns=[
    path('', views.index, name="index"),
    path("appointments/", views.list_appointments, name="list_appointments"),
    path("insert/", views.create, name="insert"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
]