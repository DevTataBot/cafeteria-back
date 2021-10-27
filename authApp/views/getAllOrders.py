from rest_framework import status, views
from ..models.order import Order
from rest_framework.response import Response
from authApp.serializers.orderSerializer import OrderSerializer
class GetAllOrders(views.APIView):
    def get(self, request, format=None):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


