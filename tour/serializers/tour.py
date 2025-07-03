from rest_framework import serializers
from ..models import Tour, TourLocation
from ..serializers.location import LocationSerializer

class TourLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = TourLocation
        fields = ['id', 'location', 'order']


class TourSerializer(serializers.ModelSerializer):
    locations = TourLocationSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = ['id', 'category', 'price', 'created_at', 'locations']
