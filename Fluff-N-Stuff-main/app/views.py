from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

#home page
def home(request):
    return render(request, "index.html")

#add product page
def add_product(request):
    form = ProductForm(request.POST or None)
    # student = Student.objects.all()
    if form.is_valid():
        form.save()
    return render(request,"add.html", {"form":form})

#show added products page
def show_product(request):
    product = Product.objects.all()
    return render(request,"show.html",{"product":product})

#update products page( WITH THE ID AND URL *possibly taking id out of all code)
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("show_product/")
    return render(request,"update.html",{"product":product})

#delete products page (WITH THE ID AND URL *possibly taking id out of all code)
def delete_product(request,pk):
    form = Product.objects.get(id=pk)
    form.delete()
    print(form)
    context={"product":form}
    return render(request, "add.html", context)

#sign up page
def sign_up(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signup')
    product = {"form": form}
    return render(request, "signup.html", product)

#login in page
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {}
    return render(request, "login.html", context)

#catalog page
def catalog(request):
    return render(request, "catalog.html")



    