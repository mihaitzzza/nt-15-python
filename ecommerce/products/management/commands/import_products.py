import json
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from products.models import Category, Product


class Command(BaseCommand):
    help = "Import products into database from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument("--file", type=str, help="Absolute path to JSON file with products data.", required=True)

    def handle(self, *args, file=None, **options):
        try:
            with open(file) as json_file:
                products_data = json.load(json_file)
        except Exception:
            raise CommandError(f"Data in file {file} is not accessible.")

        try:
            with transaction.atomic():
                for department_data in products_data:
                    # department = Category(name=department_data["name"], type="department")
                    # department.save()
                    department, _ = Category.objects.get_or_create(name=department_data["name"], type="department")

                    for category_data in department_data["categories"]:
                        category, _ = Category.objects.get_or_create(
                            parent=department,
                            # parent_id=department.id,
                            name=category_data["name"],
                            type="category"
                        )

                        for subcategory_data in category_data["categories"]:
                            subcategory, _ = Category.objects.get_or_create(
                                parent=category,
                                name=subcategory_data["name"],
                                type="subcategory"
                            )

                            for product_data in subcategory_data["products"]:
                                Product.objects.create(
                                    category=subcategory,
                                    name=product_data["title"],
                                    price=product_data["price"],
                                )
        except Exception as e:
            # raise CommandError(e)
            raise e
