from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.listProductSerializer import ListProductSerializer
from authApp.serializers.orderSerializer import OrderSerializer
from authApp.models.listProduct import ListProduct
class OrderCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            listaProductos = []
            for index in request.data['listProduct']:
                productList = ListProduct(
                    idOrden_id = serializer.data['id'],
                    idProducto_id = index['idProducto'],
                    cantidad = index['cantidad'],           
                    idUsuario_id = request.data['idUsuario']
                )
                listaProductos.append(productList)
            ListProduct.objects.bulk_create(listaProductos)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)