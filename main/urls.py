from django.urls import path
from .import views

app_name = 'main'
urlpatterns = [
    path("", views.homePageView, name='home'),
    path("detail/<slug:p_slug>/", views.detailProductView, name='detail')
]
