from django.contrib import admin
from .models import User, Product, MarketRate, Inquiry


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'phone', 'is_active', 'date_joined']
    list_filter = ['role', 'is_active', 'is_staff']
    search_fields = ['username', 'email']
    list_editable = ['is_active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'farmer', 'quantity', 'price_per_unit', 'is_available', 'created_at']
    list_filter = ['is_available', 'created_at']
    search_fields = ['name', 'description', 'farmer__username']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']


@admin.register(MarketRate)
class MarketRateAdmin(admin.ModelAdmin):
    list_display = ['crop_name', 'average_price', 'unit', 'last_updated']
    search_fields = ['crop_name']
    readonly_fields = ['last_updated']


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'product', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['buyer__username', 'product__name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'