from django.db import models


# Create your models here.


class Water(models.Model):
    water = models.CharField(max_length=100)


class Products(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductCategory = models.CharField(max_length=100)
    ProductTotalScore = models.IntegerField()
    NumberofReviews = models.IntegerField()


    @staticmethod
    def getAverageScore(self):
        avg = Products.ProductTotalScore/Products.NumberofReviews
        return avg


class Reviews(models.Model):
    ProductName = models.ForeignKey(Products, on_delete=models.CASCADE)
    ReviewScore = models.IntegerField()
    #User not working yet