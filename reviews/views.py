from django.shortcuts import render
from . models import Reviews


def product_reviews(request):
    """
    Displays all reviews of the customers

    **Context**
    ``reviews``
        An instance of :model:`reviews.Reviews`.
    **Template:**
    :template:`reviews/reviews.html`
    """
    reviews = Reviews.objects.all()

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)
