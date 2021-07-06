from django.urls import path
from .import views

from django.contrib.auth.views import LoginView


app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(
    	redirect_authenticated_user=False,
    	),
    	name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<pk>', views.UserProfileView.as_view(), name='profile'),
    path('profile/update/<pk>', views.UpdateUserProfileView.as_view(), name='update_profile'),
]