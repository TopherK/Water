from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Count


# Create your views here.


def search(request):
    products = Products.objects.all()
    context = {
        'title':"Home",
        'content': products,
        }
    return render(request, 'search.html',context)


@login_required(login_url="/login/")
def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            ProductName = form.cleaned_data['ProductName']
            ProductCategory = form.cleaned_data['ProductCategory']
            ProductFlavor = form.cleaned_data['ProductFlavor']


            post = Products.objects.create(ProductName=ProductName, ProductCategory=ProductCategory,
                                           ProductFlavor=ProductFlavor,
                                           ProductTotalScore=0, NumberofReviews=0,)
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
            element.ProductTotalScore = round(element.ProductTotalScore / element.NumberofReviews, 1)

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
            element.ProductTotalScore = round(element.ProductTotalScore / element.NumberofReviews, 1)
    for element in productsByName:
        if element.NumberofReviews != 0:
            element.ProductTotalScore = round(element.ProductTotalScore / element.NumberofReviews, 1)



    context = {
        'title': "Home",
        'content': productsByName,
        'scoreSort': productsByScore
    }
    return render(request, 'products.html', context)

@login_required(login_url="/login/")
def addReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.username = request.user
            review.save()
        prodName = request.POST.get('ProductName') #actually returns the primary key
        prodScore = request.POST.get('ReviewScore')

        #update product object
        prodObj = Products.objects.get(pk=prodName)
        prodObj.ProductTotalScore += int(prodScore)
        prodObj.NumberofReviews += 1
        prodObj.save()

        form.save()
    else:
        form = ReviewForm()

    reviews = Reviews.objects.all()

    context = {
        'title':"Home",
        'content': reviews,
        'form':form,
        }
    return render(request, 'addReview.html', context)


#from lecture example.
def displayreviews(request):
    reviews = Reviews.objects.order_by('-ReviewDate')

    context = {
        'title': "Home",
        'content': reviews,
    }
    return render(request, 'displayreviews.html', context)

def recommend(request):
    prod = Products.objects.order_by('-ProductTotalScore')
    rec = []
    for element in prod:
        if element.NumberofReviews != 0:
            element.ProductTotalScore = round(element.ProductTotalScore / element.NumberofReviews,1)
            if element.ProductTotalScore > 3:
                rec.append(element)

    context = {
        'title': "Home",
        'content': rec,
    }
    return render(request, 'recommend.html', context)

def register(request):
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1'))
            #login call back
            return HttpResponseRedirect('/')

    else:
        form = registration_form()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request, 'register.html', context)

@user_passes_test(lambda u: u.is_superuser)
def addflavor(request):
    if request.method == 'POST':
        form = FlavorsForm(request.POST)
        form.save()
    else:
        form = FlavorsForm()

    flavors = Flavors.objects.all()

    context = {
        'title':"Home",
        'content': flavors,
        'form':form,
        }
    return render(request, 'flavors.html', context)