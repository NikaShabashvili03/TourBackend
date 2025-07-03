from rest_framework import serializers
from ..models import Order
from accounts.models import User
from accounts.serializers.user import UserSerializer
from ..serializers.tour import TourSerializer
from rest_framework import serializers
from ..models import Order, Tour

class OrderSerializer(serializers.ModelSerializer):
    ordered_by = UserSerializer(read_only=True)
    tour = TourSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

class OrderCreateSerializer(serializers.Serializer):
    tour_id = serializers.IntegerField()

    def validate_tour_id(self, value):
        try:
            tour = Tour.objects.get(id=value)
        except Tour.DoesNotExist:
            raise serializers.ValidationError("Tour not found.")
        return value

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        tour = Tour.objects.get(id=validated_data['tour_id'])

        order = Order.objects.create(
            ordered_by=user,
            tour=tour,
            price=tour.price,
        )
        return order