from django.shortcuts import render, get_object_or_404, redirect
import pkg_resources
from .models import Create
from .forms import CreateForm 
# Create your views here.

# for layout 
def home(request):
    return render(request, 'app1/layout.html')

def all_product(request):
    products = Create.objects.all()
    return render(request, 'product_add/all_product.html', {'products':products})

def product_detail(request, pk):
    product = get_object_or_404(Create, pk=pk)
    return render(request, 'product_add/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_product')
    else:
        form = CreateForm()
    return render(request, 'product_add/product_create.html', {'form': form})
        
def update_product(request, pk):
    product = get_object_or_404(Create, pk=pk)
    
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_product')  
    else:
        form = CreateForm(instance=product)
    
    return render(request, 'product_add/product_form.html', {'form': form, 'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Create, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('all_product')
    return render(request, 'product_add/product_confirm_delete.html', {'product': product})