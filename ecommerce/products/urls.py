from django.urls import path
from products.views import get_all_products, get_product

app_name = "products"


urlpatterns = [
    path("", get_all_products, name="products_list"),  # http://localhost:8000/products
    path("<int:product_id>/", get_product, name="product_details"),  # http://localhost:8000/products/<product-id>
]
