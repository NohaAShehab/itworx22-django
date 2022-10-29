from django.contrib import admin
from django.urls import path, include
# from amazon.views import home_view, landing_view, user_home_view, profile_view
from cars.views import create_car_view, edit_car_view, cars_index_view
urlpatterns = [
    path("create", create_car_view, name="cars.create"),
    path("<int:id>/edit", edit_car_view, name='cars.edit'),
    path("index", cars_index_view, name="cars.index")
]