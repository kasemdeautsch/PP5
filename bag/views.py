from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view that renders the bag contents page
    **Template:**

    :template:`bag/bag.html`
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    """
    Add a quantity of the specified product to the bag
     **Context**
    ``product``
        The item to be added  :model: `products.Product`.
    ``bag``
       the shopping bag stored in the session
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = (request.POST.get('redirect_url'))

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.add_message(request, messages.SUCCESS, f'Updated {product.name} quantity to {bag[item_id]}')

    else:
        bag[item_id] = quantity
        messages.add_message(request, messages.SUCCESS, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """
    Adjust quantity of the specified product to the specified amount
    **Context**
    ``product``
        The item to be updated  :model: `products.Product`.
    ``bag``
       the shopping bag stored in the session
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if 100 > quantity > 0:
        bag[item_id] = quantity
        messages.add_message(request, messages.SUCCESS, f'Updated {product.name} quantity to {bag[item_id]}')
    elif quantity < 0:
        messages.add_message(request, messages.WARNING, f'Error!. Please enter quantity in range 1-99')
    elif quantity > 99:
        messages.add_message(request, messages.WARNING, f'Error!. Please enter quantity in range 1-99')
    else:
        bag.pop(item_id)
        messages.add_message(request, messages.SUCCESS, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    
    **Context**
    ``product``
        The item to be removed  :model: `products.Product`.
    ``bag``
       the shopping bag stored in the session
    """

    try:
        product = get_object_or_404(Product, id=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        print('request.session[bag]>>> ', request.session['bag'])
        messages.add_message(request, messages.SUCCESS, f'Removed {product.name} from your bag.')
        return HttpResponse(status=200)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Error removing item {e}')
        return HttpResponse(staus=500)
