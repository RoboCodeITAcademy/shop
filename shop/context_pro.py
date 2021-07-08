from .models import Category
from django.contrib.auth.models import User
from account.models import Profile


def view_all(request):
	
	# for i in user:
	# 	print(i.id)
	context = {
		'categories':Category.objects.all(),
		
	}
	return context