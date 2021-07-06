from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView
	)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.

# 1. TemplateView
# 2. ListView
# 3. DetailView
# 4. View
class CategoryDetailView(DetailView):
	model = Category
	# template_name = ''
	
	
class HomePageView(LoginRequiredMixin,ListView):
	login_url = '/account/login/'
	model = Product
	paginate_by = 4
	template_name = 'index.html'
	context_object_name = 'products' # object_list


class ProductDetailView(DetailView):
	model = Product

# @login_required
class CartDetailView(ListView):
	model = Product
	template_name = 'shop/cart.html'