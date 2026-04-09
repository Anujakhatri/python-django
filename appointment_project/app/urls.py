from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path("insert/", views.create, name="create"),
    path("appointments/", views.list_appointments, name="list_appointments"),
    path("edit/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
]