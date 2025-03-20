from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("cars/create/", CarCreateView.as_view(), name="car_create"),
    path("cars/<int: pk>/update/", CarUpdateView.as_view(), name="car_create"),
    path("cars/<int: pk>/delete/", CarDeleteView.as_view(), name="car_create"),

    path("cars/create/", ManufacturerCreateView.as_view(), name="car_create"),
    path("cars/<int: pk>/update/",
         ManufacturerUpdateView.as_view(), name="car_create"),
    path("cars/<int: pk>/delete/",
         ManufacturerDeleteView.as_view(), name="car_create")
]

app_name = "taxi"
