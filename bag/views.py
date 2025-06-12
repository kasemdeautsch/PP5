from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """


    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    """
    Add a quantity of the specified product to the bag
    """
    product = get_object_or_404(Product, pk=item_id)
    # product = Product.objects.get(pk=item_id)

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
    #print('request>>> ', request)
    #print('request.session>>> ', request.session)
    #print('request.session[bag]>>> ', request.session['bag'])
    return redirect(redirect_url)


def update_bag(request, item_id):
    """
    Adjust quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.add_message(request, messages.SUCCESS, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.add_message(request, messages.SUCCESS, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    #print('request>>> ', request)
    #print('request.session>>> ', request.session)
    print('request.session[bag]>>> ', request.session['bag'])
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """
    Remove the item from the shopping bag
    """

    try:
        product = get_object_or_404(Product, id=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        #print('request>>> ', request)
        #print('request.session>>> ', request.session)
        print('request.session[bag]>>> ', request.session['bag'])
        messages.add_message(request, messages.SUCCESS, f'Removed {product.name} from your bag.')
        return HttpResponse(status=200)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Error removing item {e}')
        return HttpResponse(staus=500)
