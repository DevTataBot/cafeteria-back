from django.db import models

from authApp.models.user import User
from .product import Product
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    totalPrice = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=False)
    dateOrder = models.DateTimeField(auto_now=True)