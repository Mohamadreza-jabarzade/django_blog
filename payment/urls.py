from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirm/', views.confirm_payment, name='confirm'),
    path('success/', views.success, name='success'),
]
