from django.db import models
import datetime

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

    def __str__(self):
        prodName = str(self.ProductName)
        RevScore = str(self.ReviewScore)
        RevText = self.ReviewText
        RevStr = "Product Name: " + prodName + " Review Score: " + RevScore +  "  Content: " + RevText
        return RevStr