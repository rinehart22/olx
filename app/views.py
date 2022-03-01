from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from urllib3 import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q
import datetime
from django.utils.timezone import datetime
#from .forms import SearchForm

# Create your views here.


def home(request):
    all_prod = Product.objects.all()
    return render(request, 'home.html', {'all_prod': all_prod})


@login_required(login_url='login')
def base(request):
    return render(request, 'base.html')




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


def logoutt(request):
    logout(request)

    return redirect('/login')


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


# def search_item(request):
#     item = request.GET['q']
#     # print(item)
#     search_result = Product.objects.get(product_category=item)
#     return HttpResponse(search_result)

# def search_item(request):
#     if 'q' in request.GET:
#         q = request.GET['q']
#         print(q)

#         data = category.objects.filter(
#             Q(cate__icontains=q))  # .order_by('-id')
#         mobile = mobilebrand.objects.filter(
#             Q(mb__icontains=q)).values()
#         multiple_q = Q(Q(product_name__icontains=q) | Q(
#             product_category__icontains=q) | Q(price__icontains=q) | Q(images__icontains=q))
#     else:
#         data = category.objects.all()
#     return render(request, 'search.html', {'data': data, 'mobile': mobile,  'multiple_q':  multiple_q, })
def search_item(request):
    data = request.GET['q']
    all_prod = Product.objects.filter(product_category=data)
    return render(request, 'all_prod.html', {'all_prod': all_prod})


def read_item(request, id):

    all_prod = Product.objects.get(pk=id)
    return render(request, 'read.html', {'all_prod': all_prod})


def delete(request, id):
    Product.objects.get(pk=id).delete()
    return render(request, 'delete.html')


def update(request, id):  # GET#PUT#POST
    all_prod = Product.objects.get(pk=id)
    form = ProductForm(instance=all_prod)  # old data
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=all_prod)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'update.html', {'form': form})


def categoryy(request):
    form = CategoryForm()
    if request.method == 'POST':  # TRUE

        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'category.html', context)


def create(request):
    form = ProductForm()
    if request.method == 'POST':  # TRUE

        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('/')
    return render(request, 'create.html', {'form': form})


def product(request):
    form = ProductForm()
    if request.method == 'POST':  # TRUE

        print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    return render(request, 'phone.html', {'form': form})


def all_products(request):
    all_prod = Product.objects.all()
    return render(request, 'all_prod.html', {'all_prod': all_prod})
