from django.urls import path
from .import views

from django.contrib.auth.views import LoginView

app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(
    	redirect_authenticated_user=False,

    	), name='login'),
    path('register/', views.register, name='register'),
]