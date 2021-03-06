from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.products, name='products'),
    url(r'^addproduct$', views.addproduct, name='index'),
    url(r'^top10$', views.top10, name='top10'),
    url(r'^products$', views.products, name='products'),
    url(r'^addReview$', views.addReview, name='addReview'),
    url(r'^register$',views.register, name='register'),
    url(r'^displayreviews$',views.displayreviews, name='displayreviews'),
    url(r'^flavors$',views.addflavor, name='addflavor'),
    url(r'^recommend$',views.recommend, name='recommend'),
    url(r'^addAddress$',views.addAddress, name='addAddress'),
    url(r'^location',views.location, name='location'),




]
