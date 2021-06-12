from django.shortcuts import render
from django.views.generic import TemplateView,View
# 1.TemplateView
# 2.View 
# 3.ListView
# 4.DetailView 
# Create your views here.

# class HomePageView(TemplateView):
# 	template_name = 'index.html'

class HomePageView(View):
	# Home Page view 
	#PEP8
	def get(self,request):
		return render(request, 'index.html')

		
	def post(self, request):
		return render(request, 'index.html')