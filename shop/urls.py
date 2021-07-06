from django.urls import path
from .import views


app_name = 'shop'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('detail/<pk>',
    	views.ProductDetailView.as_view(),
    	name='detail'),
    path('category/detail/<pk>',
    	views.CategoryDetailView.as_view(),
    	name='category_detail'
    	),
     path('cart/', views.CartDetailView.as_view(), name='cart')
]