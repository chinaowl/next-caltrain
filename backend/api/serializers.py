from rest_framework import serializers
from .models import Stop, Trip


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ('stop_id', 'stop_name', 'zone_id', 'platform_code')
        read_only_fields = ('stop_id', 'stop_name', 'zone_id', 'platform_code')


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('trip_id', 'route_id', 'service_id', 'trip_headsign', 'trip_short_name', 'direction_id')
        read_only_fields = ('trip_id', 'route_id', 'service_id', 'trip_headsign', 'trip_short_name', 'direction_id')
