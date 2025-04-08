from django.shortcuts import render,redirect, reverse , get_object_or_404
from django.contrib import messages
from django.db.models import Q
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

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'brand_category' in request.GET:
            brands = request.GET['brand_category'].split(',')
            print('brands1:-->', brands)
            products = products.filter(brand_category__name__in=brands)
            print('products:-->', products)
            brands = Brand.objects.filter(name__in=brands)
            print('brands2:-->', brands)

        if 'q' in request.GET:
            query = request.GET['q']
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