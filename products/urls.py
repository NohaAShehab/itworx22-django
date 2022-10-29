

from django.urls import path
from products.views import products_index_view, \
    product_details_view, create_product_view, delete_product_view, \
    edit_product_view, get_all_categories_view, get_category_view

urlpatterns = [
    path('index',products_index_view, name='products.index' ),
    path('<int:id>',product_details_view, name='products.show' ),
    path("create", create_product_view, name='product.create'),
    path("<int:id>/delete", delete_product_view, name='product.delete'),
    path("<int:id>/edit", edit_product_view, name='product.edit'),
    path("cats/index", get_all_categories_view, name='product.categories.index'),
    path("cats/<int:id>", get_category_view, name='product.categories.show'),
]