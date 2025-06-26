from django.shortcuts import render
from .models import Faqs
# Create your views here.


def answers(request):

    faqs = Faqs.objects.all()
    template = 'support/support.html'
    context = {
        'faqs': faqs,
     }

    return render(request, template, context)
