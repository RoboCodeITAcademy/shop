from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
		    # Create a new user object but avoid saving it yet
		    new_user = user_form.save(commit=False)
		    # Set the chosen password
		    new_user.set_password(user_form.cleaned_data['password'])
		    # Save the User object
		    new_user.save()
		    return redirect('account:login')
	else:
		user_form = UserRegistrationForm()
	return render(request,'registration/register.html', {'form':user_form})