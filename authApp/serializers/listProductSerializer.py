from django.db.models import fields
from rest_framework import serializers

from ..models.listProduct import ListProduct

class ListProductSerializer(serializers.ModelSerializer):
    # idOrden = serializers.RelatedField(many=True)
    class Meta:
        model = ListProduct
        fields = ['id','idOrden', 'idUsuario', 'idProducto','cantidad']