from rest_framework import serializers, status, views
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer

@api_view(['GET','PUT','DELETE'])
def updateProduct(request):
    if request.method == 'PUT':
        product = Product.objects.filter(id=request.data['id']).first()
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request, status=status.HTTP_400_BAD_REQUEST)