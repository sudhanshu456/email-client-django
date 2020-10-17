from django.urls import path

from mailclient import views

urlpatterns = [
    path("receipt_json/", views.receipt_json),
]