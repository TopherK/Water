from django.forms import ModelForm
from django import forms
from AddWater.models import Products, Reviews


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['ProductName','ProductCategory']


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['ProductName', "ReviewScore"]
