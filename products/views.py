from django.shortcuts import render,redirect, reverse , get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from products.forms import ProductForm
from .models import Product, Brand

# Create your views here.


def all_products(request):
  
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    brands = None
    sort = None
    direction = None

    if request.GET:
        #print('request.GET:-->', request.GET)
        #print('request:-->', request)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'brand':
                sortkey = 'brand__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            products = products.order_by(sortkey)
            #print('sortkey-->:', sortkey)
            #print('products-->:', products)

        if 'brand' in request.GET:
            #print("request.GET-->", request.GET.get)
            brands = request.GET['brand'].split(',')
            #print('brands1:-->', brands)
            products = products.filter(brand__name__in=brands)
            #print('products:-->', products)
            brands = Brand.objects.filter(name__in=brands)
            #print('brands2:-->', brands)

        if 'find' in request.GET:
            query = request.GET['find']
            #print("request.GET['q']:-->", request.GET.get('q','error'))

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                #url=(reverse('products'))
                #print('reverse("products"):',url)
                return redirect('/products/')
                #return redirect(('/'))
            queries = Q(name__icontains=query) | Q(processor__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_brands': brands,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.add_message(request, messages.ERROR, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated product')
            #return render(reverse('product_detail', args=[product.id]))
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Your are editing product: {product.name}')
    
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)

def delete_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Poduct deleted Successfully')
    return redirect(reverse('products'))
