from django.db import models

# Create your models here.


class Search(models.Model):
    product = models.CharField(max_length=200, null=True)

    type = models.CharField(max_length=200, null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


class category(models.Model):
    cate = models.CharField(max_length=200,default='', primary_key=True)

    def __str__(self):
        return self.cate


class product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    product_category = models.ForeignKey(
        category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product_name
