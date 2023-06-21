from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product


def get_all_products(request):
    products = Product.objects.all()

    return render(request, "products_list.html", {
        "products": products
    })


def get_product(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404(f"Product with ID = {product_id} does not exist.")

    product = get_object_or_404(Product, id=product_id)

    return render(request, "product_details.html", {
        "product": product
    })
