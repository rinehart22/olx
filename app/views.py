from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from urllib3 import HttpResponse
from . forms import SignupForm
from .models import *
from django.db.models import Q
import datetime
from django.utils.timezone import datetime
#from .forms import SearchForm

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def phone(request):
    return render(request, 'phone.html')


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                username = request.user.username

            return redirect('/')
    return render(request, 'login.html')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':  # TRUE

        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'signup.html', context)


# def search(request):
#     if 'q' in request.GET:
#        q = request.GET['q']
#         data = Data.objects.filter(last_name__icontains=q)
#         multiple_q = Q(Q(product__icontains=q) | Q(
#             type__icontains=q) | Q(date__icontains=q))

#         data = Search.objects.filter(multiple_q)
#     else:
#         data = Search.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request, 'search.html', context)


def search(request):
    item = request.GET['q']
    # print(item)
    search_result = product.objects.get(product_category=item)
    return HttpResponse(search_result)
