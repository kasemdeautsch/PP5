from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    A view that creates a shopping bag which is a list
    and returns it with other variables to be used in all templates
    """
    # Initiate an empty bag list
    bag_items = []
    total = 0
    product_count = 0

    # Get the bag from session if exist or initiate it to an empty dictionary
    bag = request.session.get('bag', {})

    # Get product from :model: `products.product`
    # Loop over bag items and generate the needed variables
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }
    return context
