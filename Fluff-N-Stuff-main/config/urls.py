"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #home page url
    path("",views.home,name= "home"),
    # add product page url
    path("add/", views.add_product, name="add_product"),
    #show added product page url
    path("show_product/", views.show_product, name= "show_product"),
    #update products page
    path("show_product/update_product/<int:pk>", views.update_product, name= "update_product"),
    #delete products page
    path("show_product/delete_product/<int:pk>/", views.delete_product, name= "delete_product"),
    #sign up page
    path("signup/", views.sign_up, name="signup"),
    #login in age
    path("signin/", views.sign_in, name="signin"),
    #catalog page
    path("catalog/", views.catalog, name="catalog")





]
