from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from products.forms import ProductForm
from .models import Product, Brand


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    **Context**
    ``product``
        An instance of :model:`products.Product`.
    ``query``
        The search query from user.
    ``products``
        All products after applying sort or search.
    ``brands``
        All brands after applying sort or search.
    ``sort``
        Current sort (brand, name, rate,...)
    ``direction``
        Direction of the sort (ascending, descending)
    ``search_term``
        The search query from the user
    ``current_brands``
        All brands
    ``current_sorting``
        current sort method plus direction
    **Template:**

    :template:`products/products.html`

    """

    products = Product.objects.all()
    query = None
    brands = None
    sort = None
    direction = None

    if request.GET:
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
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)
        if 'find' in request.GET:
            query = request.GET['find']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect('/products/')
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
    """
    A view to show individual product details
    **Context**
    ``product``
        An instance of :model:`products.Product`.
    **Template:**

    :template:`products/product_detail.html`
    """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Product admin to add products within the site
    **Context**
    ``product``
       An instance of :model:`products.Product`.
    ``form``
        an instance of :form: products.ProductForm
    **Template:**
    :template:`product/add_product.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Failed to add product! '
                                 'Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store, receiving the product_id
    **Context**
    ``product``
       An instance of :model:`products.Product`.
    ``form``
        an instance of :form: products.ProductForm
    **Template:**
    :template:`product/edit_product.html`
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. '
                                    'Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Your are editing product: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Remove a product from database, receiving the product_id.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Poduct deleted Successfully')
    return redirect(reverse('products'))
