from django.shortcuts import render
from .models import Faqs
# Create your views here.


def answers(request):
    """
    Displays frequent asks and answers

    **Context**
    ``faqs``
        All questions from :model: `support.Faqs`
    **Template:**
    :template:`support/support.html`
    """
    faqs = Faqs.objects.all()
    template = 'support/support.html'
    context = {
        'faqs': faqs,
     }

    return render(request, template, context)
