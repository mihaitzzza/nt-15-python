from django.db import models
from django.templatetags.static import static


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey("Category", null=True, default=None, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=20,
        choices=(("department", "Department"), ("category", "Category"), ("subcategory", "Subcategory")),
        default="department"
    )


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=6, decimal_places=2)  # 9999.99
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)

    def parent_subcategory(self):
        return self.category

    def parent_category(self):
        # return self.category.parent
        return self.parent_subcategory().parent

    def parent_department(self):
        # return self.category.parent.parent
        return self.parent_category().parent

    @property
    def image_src(self):
        if self.image:
            return self.image.url

        return static("images/default-product-image.png")


