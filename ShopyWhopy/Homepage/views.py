from django.shortcuts import render,get_object_or_404
from .models import Category,Product

# Create your views here.

def index(request):
    featured_products = Product.objects.filter(featured=True)[:4]
    allProducts=Product.objects.all()
    Categories=Category.objects.all()
    
    category_id = request.GET.get('Category')
    if category_id:
        allProducts = allProducts.filter(category_id=category_id)
    
    context = {
        'featured_products': featured_products,
        'allProducts': allProducts,
        'categories': Categories,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'INDEX.html',context)

def product_detail(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html',context)
