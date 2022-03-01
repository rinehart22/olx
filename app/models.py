#from turtle import title
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.


# class Search(models.Model):
#     product = models.CharField(max_length=200, null=True)

#     type = models.CharField(max_length=200, null=True)

#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.product


class category(models.Model):
    cate = models.CharField(max_length=200, default='', primary_key=True)

    def __str__(self):
        return self.cate


# class mobilebrand(models.Model):
#     mb = models.CharField(max_length=200, default='', primary_key=True)

#     def __str__(self):
#         return self.mb


class Product(models.Model):
    #
    product_name = models.CharField(max_length=200, null=True)
    product_category = models.ForeignKey(
        category, on_delete=models.CASCADE, null=True, blank=True)

    price = models.PositiveBigIntegerField(default=0)
    images = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return self.product_name

    def images_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.images.url))


# class CartOrder(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     total_amt = models.FloatField()
#     paid_status = models.BooleanField(default=False)
#     order_dt = models.DateTimeField(auto_now_add=True)
#     #order_status = models.CharField(choices=status_choice, default='process', max_length=150)

#     class Meta:
#         verbose_name_plural = '1. Orders'


# class CartOrderItems(models.Model):
#     order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
#     invoice_no = models.CharField(max_length=150)
#     item = models.CharField(max_length=150)
#     image = models.ImageField(max_length=200)
#     qty = models.IntegerField()
#     price = models.FloatField()
#     total = models.FloatField()

#     class Meta:
#         verbose_name_plural = '9. Order Items'
