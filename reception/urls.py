from django.urls import path

from reception.views import CarCreateView, CarUpdateView

urlpatterns = [
    path('car-create/', CarCreateView.as_view(), name='car-create'),
    path('car-update/<int:pk>', CarUpdateView.as_view(), name='car-update'),
]
