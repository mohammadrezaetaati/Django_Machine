from django.urls import path

from technician.views import CarRepaired

urlpatterns = [
    path('car-repaired/<int:id>', CarRepaired.as_view(), name='car-repaired'),
]
