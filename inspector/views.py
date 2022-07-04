from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Car
from core.permissions import IsInspector
from inspector.serializers import CarFinishedSerializer,AddPartCarSerializer


class CarFinished(APIView):

    permission_classes = [IsInspector]

    def post(self, request, id):
        car_obj = Car.objects.get(id=id)
        car_obj.is_finished = True
        car_obj.save()
        serializer = CarFinishedSerializer(car_obj)

        return Response(serializer.data)


class AddPartCar(APIView):

    def post(self,request,id):
        try:
            serializer=AddPartCarSerializer(data=request.data)
            if serializer.is_valid():
                part=serializer.validated_data.get('part')
                car_obj:Car=Car.objects.get(id=id)
                car_obj.part.add(part)
                return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
     
    