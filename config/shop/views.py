from django.shortcuts import render
from django.views.generic import View


class Index(View):
    def get(self, request):
        return render(request, "index.html")


class Detail(View):
    def get(self, request):
        return render(request, "detail.html")


class Shop(View):
    def get(self, request):
        return render(request, "shop.html")


class Contact(View):
    def get(self, request):
        return render(request, "contact.html")


class ShoppingCart(View):
    def get(self, request):
        return render(request, "shopping_cart.html")
    
    
class Checkout(View):
    def get(self, request):
        return render(request, "checkout.html")