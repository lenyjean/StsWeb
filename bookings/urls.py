from django.urls import path
from .views import *

urlpatterns = [
    path("bookings-list", bookings, name="bookings-list"),
    path("bookings-update/<int:pk>", bookings_update, name="bookings-update"),
    path("bookings-delete/<int:pk>", bookings_delete, name="bookings-delete"),
]