from django.shortcuts import render

from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.


def search(request):
    products = Products.objects.all()
    context = {
        'title':"Home",
        'content': products,
        }
    return render(request, 'search.html',context)


def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ProductName = form.cleaned_data['ProductName']
            ProductCategory = form.cleaned_data['ProductCategory']
            post = Products.objects.create(ProductName=ProductName, ProductCategory=ProductCategory,
                                           ProductTotalScore=0, NumberofReviews=0)
            post.save()
            # process the data in form.cleaned_data as required
            form = ProductForm()
        else:
            submit = ""
    else:
        form = ProductForm()
        submit = ""
    products = Products.objects.all()
    context = {
        'title':"Home",
        'content': products,
        'form':form,
        }
    return render(request, 'home.html', context)

def top10(request):

    prodlist = Products.objects.order_by('-ProductTotalScore')[:10]
    for element in prodlist:
        if element.NumberofReviews != 0:
            element.ProductTotalScore = element.ProductTotalScore / element.NumberofReviews

    context = {
        'title': "Home",
        'content': prodlist
    }
    return render(request, 'top10.html', context)

def products(request):
    productsByName = Products.objects.order_by('ProductName')
    productsByScore = Products.objects.order_by('-ProductTotalScore')

    for element in productsByScore:
        if element.NumberofReviews != 0:
            element.ProductTotalScore = element.ProductTotalScore / element.NumberofReviews
    for element in productsByName:
        if element.NumberofReviews != 0:
            element.ProductTotalScore = element.ProductTotalScore / element.NumberofReviews



    context = {
        'title': "Home",
        'content': productsByName,
        'scoreSort': productsByScore
    }
    return render(request, 'products.html', context)

def addReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.save()
    else:
        form = ReviewForm()

    reviews = Reviews.objects.all()

    context = {
        'title':"Home",
        'content': reviews,
        'form':form,
        }
    return render(request, 'home.html', context)