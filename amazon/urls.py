
from django.urls import path
from amazon.views import home_view, landing_view, user_home_view, \
    profile_view, amazon_home_view, contactus_view, amazon_products_view, \
    product_detail_view

urlpatterns = [
    # path('home', home_view),
    # path('', landing_view),
    path('home/profile', profile_view),
    path('home/<name>', user_home_view),
    path('home', amazon_home_view, name='amazon.home'),
    path('contactus', contactus_view, name='amazon.contactus'),
    path('productsview', amazon_products_view, name='amazon.products'),
    path("productsview/<int:product_id>/test", product_detail_view, name='amazon.products.details')

]
