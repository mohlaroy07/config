from django.urls import path

from .views import Index, Detail, Shop, Contact, ShoppingCart, Checkout


urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("detail/", Detail.as_view(), name="detail"),
    path("shop/", Shop.as_view(), name="shop"),
    path("contact/", Contact.as_view(), name="contact"),
    path("shopping-cart/", ShoppingCart.as_view(), name="shopping_cart"),
    path("checkout/", Checkout.as_view(), name="checkout"),
]