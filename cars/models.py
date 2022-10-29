from django.db import models
from django.shortcuts import get_object_or_404, reverse

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='cars/images/')
    price = models.IntegerField(default=1000)
    in_stock = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, related_name='brand_cars', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_object(cls, id):
        return get_object_or_404(cls, pk=id)


    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()


    def get_edit_url(self):
        url = reverse("cars.edit", args=[self.id])
        return url
