from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request):  # http request
    return HttpResponse("Amazon home page ")


def landing_view(request):
    return HttpResponse("<h1 style='color:red'> --- Django Landing page ---</h1>")


def user_home_view(request, name):
    return HttpResponse(f"<h1> Hi {name}</h1>")


def profile_view(request):
    return HttpResponse("<h1> ---------------------Profile------------------------------</h1>")


def amazon_home_view(request):
    return render(request, "amazon/home.html")


def contactus_view(request):
    return  render(request, "amazon/contactus.html")



def amazon_products_view(request):
    allproducts  = [
        {"name":"book", "img":'img1.png'},
        {"name":"flower", 'img':'img1.png'}
    ]

    return render(request, "amazon/amazonproducts.html",context={"products":allproducts} )