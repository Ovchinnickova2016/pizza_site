from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})