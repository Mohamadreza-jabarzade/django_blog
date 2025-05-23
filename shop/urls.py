from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('cart/', views.cart_view, name='cart'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('add-to-cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:course_id>/', views.remove_from_cart, name='remove_from_cart'),
]
