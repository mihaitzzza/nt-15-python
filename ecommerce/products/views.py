from django.shortcuts import render, Http404

products = [
    {
        "id": 1,
        "name": "Laptop #1",
        "price": 200.00
    },
    {
        "id": 2,
        "name": "Laptop #2",
        "price": 1200.00
    },
    {
        "id": 3,
        "name": "Laptop #3",
        "price": 80.00
    }
]


def get_all_products(request):
    return render(request, "products_list.html", {
        "products": products
    })


def get_product(request, product_id):
    filtered_products = [
        product for product in products if product["id"] == product_id
    ]

    if len(filtered_products) == 0:
        raise Http404(f"Product with ID = {product_id} does not exist.")

    return render(request, "product_details.html", {
        "product": filtered_products[0]
    })
