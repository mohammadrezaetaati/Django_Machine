from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from core.models import Car, CarPart


class CarFinishedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['car_name', 'is_finished']
        extra_kwargs = {
            "car_name": {"read_only": True}
        }


class AddPartCarSerializer(serializers.ModelSerializer):

    class Meta:
        model=CarPart
        fields=['part_name']