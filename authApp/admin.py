from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.product import Product
from .models.order import Order

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)