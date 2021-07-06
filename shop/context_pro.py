from .models import Category
from django.contrib.auth.models import User
from account.models import Profile


def view_all(request):
	user = Profile.objects.get(id=request.user.id)
	print(user.id)
	# for i in user:
	# 	print(i.id)
	context = {
		'categories':Category.objects.all(),
		'user':user
	}
	return context