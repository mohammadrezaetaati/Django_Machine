from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Car
from core.permissions import IsTechnician
from technician.serializers import CarRepairedSerializer


class CarRepaired(APIView):
    permission_classes = [IsTechnician]

    def post(self, request, id):
        car_obj = Car.objects.get(id=id)
        serializer = CarRepairedSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['is_repair'] == True:
                car_obj.is_repair = True
                car_obj.save()
                return Response(status=status.HTTP_201_CREATED)
            elif serializer.validated_data['is_repair'] == False:
                car_obj.is_repair = False
                car_obj.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
