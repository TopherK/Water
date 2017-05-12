from django.forms import ModelForm
from django import forms
from AddWater.models import Products, Reviews, Flavors, Address
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['ProductName','ProductCategory','ProductPHBalance','ProductFlavor']

class FlavorsForm(ModelForm):
    class Meta:
        model = Flavors
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
        exclude = ('username',)
    #this is to make the ReviewForm show the ProductNames in alpabetical order
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['ProductName'].queryset = Products.objects.order_by('ProductName')

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields ='__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Address
        fields = ['ProductName']
#from lecture example
class registration_form(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
class LoginForm(AuthenticationForm):
     username=forms.CharField(
         label="Username",
         max_length=30,
         widget=forms.TextInput(attrs={
             'class': 'form-control',
             'name':'username'
         })
     )
     password=forms.CharField(
         label="Password",
         max_length=32,
         widget=forms.PasswordInput()
     )