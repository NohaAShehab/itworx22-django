

from django.urls import path
from employees.views import home_view
urlpatterns = [

    path('home', home_view)
]