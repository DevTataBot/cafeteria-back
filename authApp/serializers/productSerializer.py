from django.db.models import fields
from authApp.models.product import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','nombre', 'unitPrice', 'unidadesTotales']
        