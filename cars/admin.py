from django.contrib import admin

# Register your models here.
from cars.models import Car, Brand
admin.site.register(Car)
admin.site.register(Brand)