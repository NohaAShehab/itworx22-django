from django.shortcuts import render, redirect
from cars.models import Car
# Create your views here.
from cars.forms import  CarForm, CarModelForm
from django.http import  HttpResponse

#


def create_car_view(request):
    if request.POST:
        myform =CarModelForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return HttpResponse("car added ")

    car_form = CarModelForm()
    return render(request, "cars/create.html", context={"form":car_form})



def edit_car_view(request, id):
    car = Car.get_object(id)
    if request.POST:
        form = CarModelForm(request.POST,request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("cars.index")
        else:
            return HttpResponse("Form not valid ")



    myform = CarModelForm(instance=car)
    return render(request, "cars/edit.html", context={"form":myform, "img":car.image})


def cars_index_view(request):
    cars = Car.get_all_objects()
    return render(request, "cars/index.html", context={"cars":cars})







