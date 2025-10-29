from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='agri/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Farmer routes
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('farmer/product/add/', views.product_add, name='product_add'),
    path('farmer/product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('farmer/product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Buyer routes
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    
    # Product routes
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Inquiry routes
    path('product/<int:pk>/inquiry/', views.send_inquiry, name='send_inquiry'),
    path('inquiries/', views.my_inquiries, name='my_inquiries'),
    path('inquiry/<int:pk>/status/<str:status>/', views.update_inquiry_status, name='update_inquiry_status'),
    
    # Market rates
    path('market-rates/', views.market_rates, name='market_rates'),
    
    # Contact
    path('contact/', views.contact, name='contact'),
]
