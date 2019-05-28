from django.contrib import admin
from .models import Products, Orders, All_orders
# Register your models here.
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(All_orders)
