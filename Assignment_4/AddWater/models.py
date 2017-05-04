from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Water(models.Model):
    water = models.CharField(max_length=100)


class Products(models.Model):
    ProductName = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
        ('Sparkling', 'Sparkling'),
        ('Flat', 'Flat'),
    )
    ProductCategory = models.CharField(max_length=9, choices=CATEGORY_CHOICES)
    ProductTotalScore = models.PositiveSmallIntegerField()
    NumberofReviews = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ProductName


class Reviews(models.Model):
    ProductName = models.ForeignKey(Products)
    ReviewScore = models.PositiveSmallIntegerField()
    ReviewText = models.TextField()
    ReviewDate = models.DateTimeField(auto_now_add=True, db_index=True)
    username = models.ForeignKey(User)

    def __str__(self):
        prodName = str(self.ProductName)
        RevScore = str(self.ReviewScore)
        RevText = self.ReviewText
        RevStr = "Product Name: " + prodName + " Review Score: " + RevScore +  "  Content: " + RevText
        return RevStr

class Flavors(models.Model):
    ProductName = models.ForeignKey(Products)
    ProductFlavor = models.CharField(max_length=15)
    username = models.ForeignKey(User)