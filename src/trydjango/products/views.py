from django.shortcuts import render
from .models import Product
from .form import RawProductForm, ProductForm
# Create your views here.

# def product_create_view(request) : 
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             print('data ', form_data)
#             Product.objects.create(**form_data)
#         else :
#             print(form.errors)
#     context = {
#         'form' : form
#     }
#     return render(request, 'products/product_create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_detail_view(request) :
    obj = Product.objects.get(id=1)
    context = {
        'product':obj
    }
    return render(request, 'products/product_detail.html', context)