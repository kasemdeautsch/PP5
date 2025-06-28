from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents
from products.models import Product
from .models import OrderLineItem, Order
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    A view to update the payment intent on post with some usefull infos
    **Context**
    ``pid``
        payment intent created by checkout view.
    ``bag``
        shopping bag from the session.
    ``save_info``
        get the value of save_info if user wants to save his profile.
   ``username``
        username from the reqwuest object
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Creates payment intent first on 'GET' and fetches the user profile
    if user is logged in and render it,
    On 'POST' creates the order with lineitems
    in the database :model: `checkout.Order` :model: `products.Product`.
    :model: `profiles.UserProfile`.
    redirects to a success page on success.
    **Context**
    ``oredr_form``
        An instance of :form: `checkout.OrderForm`.
    ``stripe_public_key``
        stored in enviroment
    ``stripe_secret_key``
        stored in enviroment
    **Template:**
    :template: `checkout/checkout.html`.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.add_message(request, messages.ERROR, (
                        "One of the products in your bag wasn't found "
                        "in our database. "
                        "Call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.add_message(request, messages.ERROR, (
                        "There was an error in in your form. "
                        "Please check the for again")
                    )
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.add_message(request, messages.ERROR,
                                 "There's nothing in your bag at the moment")
            return redirect(reverse('products'))
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1':  profile.default_street_address1,
                    'street_address2':  profile.default_street_address2,
                    'county':  profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
        if not stripe_public_key:
            messages.add_message(request, messages.WARNING,
                                 'Stripe public key is missing, \
                did you forget to set it in your Enviroment?')
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkout attaches user profile on order
    if user is logged in and saves user's infos
    when user chooses to save his infos
    for the next ordering
    **Context**
    ``order``
        The order of the customer with 'order_number'
        :model: `checkout.Order`.
    **Template:**
    :template: `'checkout/checkout_success.html`.

    """
    # if user wants to save his info
    save_info = request.session.get('save_info')
    # Get the user's order
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        # Attach user's profile to the order
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()
        # save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
    messages.success(request, f'Order successful! \
                     Your order number is: "{order_number}", A confirmation \
                        Email will be sent to {order.email}')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
