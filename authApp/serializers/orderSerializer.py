from django.db.models import fields
from authApp.models.order import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','cantidad', 'totalPrice', 'idUsuario','dateOrder']


        