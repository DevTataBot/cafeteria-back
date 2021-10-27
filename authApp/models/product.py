from django.db import models
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64, null=False)
    unitPrice = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=False)
    unidadesTotales = models.IntegerField(default=0)