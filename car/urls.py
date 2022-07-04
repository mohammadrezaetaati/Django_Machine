from django.urls import path

from car.views import CarListView, CarDetailView, PartListView

urlpatterns = [
    path('car-list/', CarListView.as_view(), name='car-list'),
    path('car-detail/<int:pk>', CarDetailView.as_view(), name='car-detail'),
    path('part-list/', PartListView.as_view(), name='part-list'),
]
