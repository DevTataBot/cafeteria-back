from rest_framework import status, views
from ..models.product import Product
from rest_framework.response import Response
from authApp.serializers.productSerializer import ProductSerializer
class MenuDetailView(views.APIView):
    def get(self, request, format=None):
        menu = Product.objects.all()
        serializer = ProductSerializer(menu, many=True)
        return Response(serializer.data)