from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from api.models.Order import Order, OrderItem

# Register your models here.    

admin.site.register(User, UserAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)