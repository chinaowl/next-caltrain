# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Stop(models.Model):
    stop_id = models.IntegerField(primary_key=True)
    stop_code = models.IntegerField(null=True)
    stop_name = models.CharField(max_length=128, null=True)
    stop_desc = models.CharField(max_length=128, null=True)
    stop_lat = models.FloatField(null=True)
    stop_lon = models.FloatField(null=True)
    zone_id = models.SmallIntegerField(null=True)
    stop_url = models.CharField(max_length=128, null=True)
    location_type = models.SmallIntegerField(null=True)
    parent_station = models.IntegerField(null=True)
    platform_code = models.CharField(max_length=2, null=True)
    wheelchair_boarding = models.SmallIntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'stop'


class StopTime(models.Model):
    trip_id = models.CharField(max_length=128, null=True)
    arrival_time = models.TextField(null=True)  # This field type is a guess.
    departure_time = models.TextField(null=True)  # This field type is a guess.
    stop_id = models.IntegerField(null=True)
    stop_sequence = models.SmallIntegerField(null=True)
    pickup_type = models.SmallIntegerField(null=True)
    drop_off_type = models.SmallIntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'stop_time'


class Trip(models.Model):
    route_id = models.CharField(max_length=128, null=True)
    service_id = models.CharField(max_length=128, null=True)
    trip_id = models.CharField(max_length=128, primary_key=True)
    trip_headsign = models.CharField(max_length=128, null=True)
    trip_short_name = models.SmallIntegerField(null=True)
    direction_id = models.SmallIntegerField(null=True)
    block_id = models.CharField(max_length=128, null=True)
    shape_id = models.CharField(max_length=128, null=True)
    wheelchair_accessible = models.SmallIntegerField(null=True)
    bikes_allowed = models.SmallIntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'trip'
