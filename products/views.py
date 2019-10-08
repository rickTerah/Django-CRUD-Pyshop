from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_list_view(request):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def product_detail_view(request, id):
    template_name = 'product_detail.html'
    obj = Product.objects.get(id=id)
    context = {
        "object": obj,
    }
    return render(request, template_name, context)

def product_create_view(request):
    template_name = 'product_create.html'
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, template_name, context)

def product_update_view(request, id):
    template_name = 'product_create.html'
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, template_name, context)

def product_delete_view(request, id):
    template_name = 'product_delete.html'
    obj = Product.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj
    }
    
    return render(request, template_name, context)