from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.forms import *

from .models import *

# Create your views here.
@login_required(login_url='/accounts/login')
def products(request):
    template_name = "products/products_list.html"
    available_products = Products.objects.filter(status="Available")
    not_available_products = Products.objects.filter(status="Not Available")
    
    context = {
        "available_products": available_products,
        "not_available_products" : not_available_products,
        "products_state": "background-color: #dbeafe;"
    }
    return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def products_add(request):
    template_name = "products/products_add.html"
    form = ProductForms(request.POST or None)
    if form.is_valid():
        new_product = form.save(commit=False)
        new_product.status = "Available"
        new_product.save()
        return redirect("products-list")
    context = {
       "form" :  form,
        "products_state": "background-color: #dbeafe;"
    }
    return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def products_view(request, pk):
     template_name = "products/products_view.html"
     products = Products.objects.filter(id=pk)
     context = {
         "products" : products,
        "products_state": "background-color: #dbeafe;"
     }
     return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def products_update(request, pk):
    template_name = "products/products_update.html"
    products = get_object_or_404(Products, pk=pk)
    form = ProductForms(request.POST or None, instance=products)
    if form.is_valid():
         form.save()
         return redirect("products-list")
    context = {
        "form" : form,
        "products_state": "background-color: #dbeafe;"
    }
    return render (request, template_name, context)
    
@login_required(login_url='/accounts/login')
def products_delete(request, pk):
    products = Products.objects.filter(id=pk).update(status="Not Available")
    return redirect("products-list")
