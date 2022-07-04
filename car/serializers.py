from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import serializers

from core.models import Car, CarPart


class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarPart
        fields = ['part_name']


class ReciptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'


class ReciptionDetailSerializer(serializers.ModelSerializer):

    part = PartSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = ['car_name', 'part', 'is_finished', 'is_repair']


class PartListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarPart
        fields = '__all__'
