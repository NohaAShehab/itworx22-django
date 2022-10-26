from django.shortcuts import render, redirect , reverse, get_object_or_404
from django.http import HttpResponse
from products.models import Product


# Create your views here.

## create view that displays all data from the table products


def products_index_view(request):
    # products = Product.objects.all()
    products= Product.get_all_object()
    # return HttpResponse(products)
    return render(request, "products/index.html", context={"products": products})


def product_details_view(request, id):
    # product = Product.objects.get(pk=id)
    # product = get_object_or_404(Product, pk=id)
    product = Product.get_object(id)
    return render(request, "products/show.html", context={"product": product})


def create_product_view(request):
    if request.POST:
        p = Product()
        print(request.POST)
        print(request.FILES)
        # name = request.POST["name"]
        if request.POST["name"] != " ":
            p.name = request.POST["name"]
        else:
            return HttpResponse("please provide ")
        p.no_of_items = request.POST.get("no_of_items")
        p.img = request.POST["img"]
        p.value = request.POST["value"]
        p.description = request.POST["description"]
        if "in_stock" in request.POST:
            p.in_stock = True

        if request.FILES:
            image = request.FILES["image"]
            from time import time
            timestampe= time()
            image.name =f"{timestampe}{image.name}"
            print(image, type(image), image.name)
            p.image = image

        p.save()
        # print(p.id)
        # redirected_url = reverse('products.index')
        # redirected_url = reverse("products.show", args=[p.id])
        # redirected_url  +="?name=shehab"
        # return redirect(redirected_url)
        # return HttpResponse(f"POST request received , New object added : {p.id}")
        ## 'products.index' ==? convert to http::127.0.0.1/products/index
        # url =  reverse("products.show", args=[p.id])
        # return redirect(url)
        # return redirect("products.show",p.id)
        return redirect(p.get_show_url())



    return render(request, "products/create.html")



def delete_product_view(request, id):
    Product.delete_object(id)
    return redirect("products.index")


def edit_product_view(request, id):
    product = Product.get_object(id)

    if request.POST:
        product.name = request.POST["name"]
        product.no_of_items = request.POST.get("no_of_items")
        product.value = request.POST["value"]
        product.description = request.POST["description"]
        if "in_stock" in request.POST:
            product.in_stock = True
        if request.FILES:
            image = request.FILES["image"]
            from time import time
            timestampe = time()
            image.name = f"{timestampe}{image.name}"
            print(image, type(image), image.name)
            product.image = image

        product.save()

        return redirect(product.get_show_url())



    return render(request, "products/edit.html", context={"product":product})










