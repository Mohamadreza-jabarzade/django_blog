from django.contrib import admin
from .models import Purchase
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali

@admin.register(Purchase)
class PurchaseAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['tracking_code', 'email', 'phone', 'product_name', 'shamsi_date']

    def shamsi_date(self, obj):
        return datetime2jalali(obj.created_at).strftime('%Y/%m/%d')
    shamsi_date.short_description = 'تاریخ'
