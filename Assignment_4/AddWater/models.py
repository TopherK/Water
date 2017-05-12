from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Flavors(models.Model):
    ProductFlavor = models.CharField(max_length=15)
    def __str__(self):
        return self.ProductFlavor


class Products(models.Model):
    ProductName = models.CharField(max_length=100, unique=True)
    CATEGORY_CHOICES = (
        ('Sparkling', 'Sparkling'),
        ('Flat', 'Flat'),
    )
    ProductCategory = models.CharField(max_length=9, choices=CATEGORY_CHOICES)
    ProductTotalScore = models.PositiveSmallIntegerField()
    NumberofReviews = models.PositiveSmallIntegerField()
    ProductFlavor = models.ForeignKey(Flavors)
    ProductTotalHydrationFactor = models.PositiveIntegerField(default=0)

    PH_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
    )
    INT_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    ProductPHBalance = models.PositiveSmallIntegerField(default=7, choices=PH_CHOICES)
    def __str__(self):
        return self.ProductName

class Reviews(models.Model):
    ProductName = models.ForeignKey(Products)
    CATEGORY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    ReviewScore = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)
    HydrationFactor = models.PositiveSmallIntegerField(default=1, choices=CATEGORY_CHOICES)
    ReviewText = models.TextField()
    ReviewDate = models.DateTimeField(auto_now_add=True, db_index=True)
    username = models.ForeignKey(User)

    def __str__(self):
        prodName = str(self.ProductName)
        RevScore = str(self.ReviewScore)
        RevText = self.ReviewText
        RevStr = "Product Name: " + prodName + " Review Score: " + RevScore +  "  Content: " + RevText
        return RevStr

class Address(models.Model):
    ProductName = models.ForeignKey(Products)
    address = models.CharField(max_length=200)
    def __str__(self):
        return  self.address

