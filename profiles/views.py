from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm
# Create your views here.


def profile(request):
    """
    Displays the user's profile
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile updated successfully')
    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)
    # order = Order.objects.get(order_number=order_number)
    messages.add_message(request, messages.INFO, (
        f'This is a past confirmation for order number {order_number}. '
        f'A confirmation email was sent on the order date'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }
    return render(request, template, context)