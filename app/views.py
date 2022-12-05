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

#update products page(DOESN'T WORK YET SOMETHING IS WRONG WITH THE ID AND URL)
def update_product(request,pk):
    product = Product.objects.get(customer_id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=product)
        print(form.is_valid())
        if form.is_valid():
            form.save()
    return render(request,"update.html",{"product":product})

#delete products page (DOESN'T WORK YET SAME THING AS UPDATE)
def delete_product(request,pk):
    form = Product.objects.get(customer_id=pk)
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


    