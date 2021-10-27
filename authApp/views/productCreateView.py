from rest_framework import serializers, status, views
from rest_framework.response import Response
from authApp.models.product import Product
from authApp.serializers.productSerializer import ProductSerializer
class ProductCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    