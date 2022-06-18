from django.shortcuts import render
from .models import Product
# Create your views here.


def homePageView(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def detailProductView(request, p_slug):
    product = Product.objects.get(slug=p_slug)
    return render(request, "detail.html", {"product": product})
