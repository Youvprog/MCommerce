from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('store',views.store, name="store"),
    path('result', views.search, name="search"),
    path('result/cart', views.cart, name="cart")
]
