from django.urls import path

from inspector.views import CarFinished,AddPartCar

urlpatterns = [
    path('car-finished/<int:id>', CarFinished.as_view(), name='car-finished'),
    path('car-add-par/<int:id>', AddPartCar.as_view(), name='car-add-part'),
]
