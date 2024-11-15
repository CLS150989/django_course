from django.urls import path
from django.urls import path
from .views import AddProductView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", AddProductView.as_view(), name= 'add_product')
]