from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Order
from ..serializers.order import OrderSerializer, OrderCreateSerializer
from accounts.permissions import AllowAny, IsAuthenticated

class OrderFeedView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
class OrderCreateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        order = serializer.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)