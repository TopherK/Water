from django.forms import ModelForm
from AddWater.models import Products


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['ProductName','ProductCategory']
