# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .models import Stop, Trip
from .serializers import StopSerializer, TripSerializer


class StopsView(generics.ListCreateAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer


class TripsView(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
