from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
# Create your views here.

# 1. TemplateView
# 2. ListView
# 3. DetailView
# 4. View

class HomePageView(ListView):
	model = Product
	template_name = 'index.html'
	context_object_name = 'products' # object_list