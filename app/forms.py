
from .models import *

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.forms import ModelForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class SellForm(forms.ModelForm):
 #   product = forms.CharField(label='')

  #  class Meta:
   #     model = Search
    #    fields = ['product', ]

class CategoryForm(ModelForm):
    class Meta:
        model = category
        fields = '__all__'

# ProfileEdit


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
