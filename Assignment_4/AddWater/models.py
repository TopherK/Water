from django.db import models


# Create your models here.


class Water(models.Model):
    water = models.CharField(max_length=100)


class Products(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductCategory = models.CharField(max_length=100)
    ProductTotalScore = models.PositiveSmallIntegerField()
    NumberofReviews = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ProductName


class Reviews(models.Model):
    ProductName = models.ForeignKey(Products)
    ReviewScore = models.PositiveSmallIntegerField()
    ReviewText = models.TextField()