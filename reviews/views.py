from django.shortcuts import render
from . models import Reviews
# Create your views here.


def product_reviews(request):

    reviews = Reviews.objects.all()

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }

    return render(request, template, context)
