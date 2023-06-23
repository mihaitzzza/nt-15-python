from django import forms
from products.models import Product


class ProductsByPrice(forms.Form):
    min_price = forms.IntegerField(required=False, step_size=100, label="Min", min_value=0)
    max_price = forms.IntegerField(required=False, step_size=100, label="Max", min_value=0)

    def clean(self):
        min_price = self.cleaned_data.get("min_price", 0)
        max_price = self.cleaned_data.get("max_price", 0)

        if min_price == 300 and max_price == 200:
            raise forms.ValidationError({
                "min_price": "Min price hardcoded value invalid!",
                "max_price": "Max price hardcoded value invalid!",
            })

        return {
            "min_price": min_price,
            "max_price": max_price,
        }

    def clean_max_price(self):
        min_price = self.cleaned_data.get("min_price", 0)
        max_price = self.cleaned_data.get("max_price", 0)

        if max_price < min_price:
            raise forms.ValidationError("max_price cannot be lower than min_price!")

        return max_price

    def get_filtered_products(self):
        products = Product.objects

        min_price = self.cleaned_data.get("min_price")
        max_price = self.cleaned_data.get("max_price")
        print('\n' * 2)
        print('max_price', max_price)
        print('\n' * 2)

        if min_price:
            products = products.filter(price__gte=min_price)

        if max_price:
            products = products.filter(price__lte=max_price)

        return products.all()
