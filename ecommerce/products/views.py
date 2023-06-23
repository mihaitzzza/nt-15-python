from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product
from products.forms import ProductsByPrice


# def get_all_products(request):
#     min_price = request.GET.get("min")
#     max_price = request.GET.get("max")
#
#     # products = Product.objects.all()
#     # products = Product.objects.filter(price=2099.99).all()
#     # products = Product.objects.filter(price__gte=min_price, price__lte=max_price).all()
#     products = Product.objects
#     if min_price:
#         products = products.filter(price__gte=min_price)
#     if max_price:
#         products = products.filter(price__lte=max_price)
#
#     return render(request, "products_list.html", {
#         "products": products.all()
#     })
def get_all_products(request):
    form = ProductsByPrice(request.GET)
    if form.is_valid():
        products = form.get_filtered_products()
    else:
        products = []

    return render(request, "products_list.html", {
        "products": products,
        "form": form,
    })


def get_product(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404(f"Product with ID = {product_id} does not exist.")

    product = get_object_or_404(Product, pk=product_id)
    # product = get_object_or_404(Product, id=product_id)

    return render(request, "product_details.html", {
        "product": product
    })
