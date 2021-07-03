from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView
	)
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

# 1. TemplateView
# 2. ListView
# 3. DetailView
# 4. View
class CategoryDetailView(DetailView):
	model = Category
	# template_name = ''
	
	
class HomePageView(ListView,):
	model = Product
	template_name = 'index.html'
	context_object_name = 'products' # object_list


class ProductDetailView(DetailView):
	model = Product

# @login_required
def test_user(request):
	if request.user.is_authenticated:
		return render(request, 'shop/product_detail.html')
	else:
		return HttpResponseForbidden('Ruxsat yo')