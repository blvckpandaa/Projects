from django.contrib import admin
from .models import *


admin.site.register(Food)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderProduct)