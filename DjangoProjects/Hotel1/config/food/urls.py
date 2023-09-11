from django.urls import path 
from .views import *
urlpatterns = [
    path('food/', food_list, name='food'),
    path('cart/', cart, name='cart'),
    path('delete_cart_item/<int:pk>', delete_cart_item, name="delete_cart_item"),
    path('edit_cart_item/<int:pk>', edit_cart_item, name="edit_cart_item"),
    path('cart/order', order, name='order'),
    path('orders/', orders, name='orders'),
    path('delete_order/<int:pk>', delete_order, name='delete_order'),
]