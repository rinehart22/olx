from unicodedata import category
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Search)
admin.site.register(category)
admin.site.register(product)

