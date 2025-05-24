from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'email', 'phone', 'product_name', 'created_at')
    search_fields = ('email', 'tracking_code', 'phone', 'product_name')
