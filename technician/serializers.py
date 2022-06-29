from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework import serializers

from core.models import Car


class CarRepairedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['is_repair']


