from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import SignupForm 
from .models import Search
from .forms import SearchForm

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


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


def signup(request):
    form = SignupForm()
    if request.method == 'POST':  # TRUE

        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'signup.html', context) 


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
