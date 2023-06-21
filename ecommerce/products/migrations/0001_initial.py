# Generated by Django 4.2.2 on 2023-06-20 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("department", "Department"),
                            ("category", "Category"),
                            ("subcategory", "Subcategory"),
                        ],
                        default="department",
                        max_length=20,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.category",
                    ),
                ),
            ],
        ),
    ]