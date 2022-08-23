from calendar import c
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
from django.contrib import messages

def home(request):

    CRITICAL = 5
    all_prod = Product.objects.all()
    
    ad = Product.objects.filter(price__icontains='1000000')
    print() # <QuerySet [<Product: yamaha r1 M>

    d = Product.objects.filter(price__iexact='455')
    print()  # <QuerySet [<Product: yamaha r1 M>]

    e = Product.objects.filter(price__in='15000')
    print()  # <QuerySet [<Product: yamaha r1 M>]

    union = ad.union(d)
    print(union)

    result = ad | d 
    print(result, '-------------------')

    var = list(chain(ad,d))
    print(var, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')




    # using not query   User.objects.filter(~Q(id__lt=5))

    all = Product.objects.filter(~Q(id__lt=8)) #it restrict objects below lessthan 8
    print(all)# QuerySet [<Product: ramb>]

    a  = Product.objects.all().values('mod','price','id')
    print(a)# <QuerySet [{'mod': 'r1', 'price': 1000000, 'id': 4},
    print()

    aa  = Product.objects.all().only('id')
    print(aa) #<QuerySet [<Product: yamaha r1 M>, <Product: auto>
    print()
    av  = Product.objects.all().values_list('id','price')
    print(av)  #<QuerySet [(4, 1000000), (5, 9500000)
    print(str(all_prod.query)) # it displays sql query syntax
    print()
    print('vvvvvvvvvvv')

    al = Product.objects.all().aggregate(Avg('price'))
    print() # {'price__avg': 2628863.75}

    als = Product.objects.all().aggregate(Sum('price'))
    print()  #{'price__sum': 10515455}
    ac = Product.objects.all().aggregate(Count('price'))
    ao = Product.objects.all().order_by('-price')[0]
    am = Product.objects.all().order_by(Lower('mod'))
    
    print()
    print()
    print()
    print()

    ex = Product.objects.filter(price__exact=15000) # [<Product: smartphone Mi A3>, <Product: iphone>]>
    print()
    exg = Product.objects.get(id__iexact=8) # iphone
    print()
    
    nan = Product.objects.filter(mod__icontains='A4')
    print()
    p =Product.objects.filter(product_name__startswith='iphone')
    

    all_prod = Product.objects.all()
    messages.success(request, 'Three credits remain in your account.')
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
#         q = request.GET['q']
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

#     # data = Product.objects.all().order_by("product_Name")
#     query = request.GET["q"]
#     if query is not None:
#         data = all_products.filter(Q(product_Name__icontains=query) |Q(product_category__icontains=query)).distinct()
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     print(q)

    #     # data = category.objects.filter(Q(cate__icontains=q))  # .order_by('-id')
    #     #x = Q(mb__icontains=q)
        
    #     multiple_q = Q(Q(product_name__icontains=q) | Q(product_category__icontains=q) | Q(price__icontains=q) | Q(images__icontains=q))
    #     data = Product.objects.filter(multiple_q).values()
    # else:
    #     data = Product.objects.all()
        # return render(request, 'all_prod.html', { 'data': data })


#this correct one 
# def search_item(request):
#     data = request.GET['q']
#     if data is not None:
#     # all_prod = Product.objects.filter(price=data)
#         all_prod = Product.objects.filter(price__icontains=data)
#         all = Product.objects.filter(product_name__icontains=data)
        
#         # all = Product.objects.filter(product_category=data)
#     return render(request, 'all_prod.html', {'all_prod': all_prod, 'all': all})



def search_it(request):
    all_prod = Product.objects.all()
    if request.method == 'GET':
        #breakpoint()
        query= request.GET.get('q')
        #submitbutton= request.GET.get('submit')
        #data = category.objects.get(cate=query)
        
        #print(data)
        
        if query is not None:
            lookups= Q(price__icontains=query) | Q( product_name__icontains=query) | Q( mod__icontains=query) | Q(product_category=query)

            results= Product.objects.filter(lookups).distinct()

            context={'results': results
                     }

            return render(request, 'home.html', context)

    else:
        return render(request, 'home.html')








# def search_item(request):
#     if request.method == 'POST':
#         q = request.POST['q']
#         s = Product.objects.filter(price__icontains=q)
#         return render(request, 'all_prod.html', {'q': q, 's': s})
















# q = request.GET['q']
# if q is not None:

#     query = t.objects.filter(Q(id__icontains=q) | Q(title__icontains=q) | Q(url__icontains=q))
#     return render(request, 'search/results_table.html', {'tbl_name': table_name,
#                                                          'details': query,
#                                                          'query': q})

# else:
#     return HttpResponse("Please submit a search term!")





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
