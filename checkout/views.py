from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    bag = request.session.get('bag', {})
    if not bag:
        messages.add_message(request, messages.ERROR, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total= round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RZUB0PSaDnciGD0sUTsZISSLTIr3pNb1G2ZtjKtPXSpa9Eoza9Lspk2QtJrGcqOx3JGUuHR3326RJcOX63ScIBl00cpDtnMhw',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)