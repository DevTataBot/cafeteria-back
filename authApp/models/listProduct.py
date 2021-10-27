from django.db import models
from authApp.models.order import Order
from authApp.models.user import User

from .product import Product

class ListProduct(models.Model):
    id = models.AutoField(primary_key=True)
    idOrden = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=0)