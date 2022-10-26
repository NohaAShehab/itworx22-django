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
    return render(request, "amazon/contactus.html")


allproducts = [
    {"id": 1, "name": "book", "img": 'img1.png', "description": "book1 description"},
    {"id": 2, "name": "flower", 'img': 'img2.png', "description": "book2 description"},
]


def amazon_products_view(request):
    return render(request, "amazon/amazonproducts.html", context={"products": allproducts})


def product_detail_view(request, product_id):
    # get the product related to the given Id
    print(type(product_id))
    for product in allproducts:
        if product["id"] == product_id:
            selected_product = product
            # return HttpResponse(selected_product["name"])
            return render(request, "amazon/showproduct.html", context={"product":selected_product})
    else:
        return HttpResponse("product not found ")
