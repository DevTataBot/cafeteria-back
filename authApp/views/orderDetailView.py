from rest_framework import status, views
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from authApp.serializers.orderSerializer import OrderSerializer
from ..models.order import Order
from rest_framework.response import Response

@api_view(['GET','PUT','DELETE'])
def getOrders(request,pk):
    if request.method == 'GET':
        order = Order.objects.filter(idUsuario = pk).all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
    return Response(request)