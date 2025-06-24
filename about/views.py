from django.shortcuts import render
from django.contrib import messages
from .models import About, CollaborateRequest
from .forms import CollaborateForm
# Create your views here.


def about_developer(request):
    """
    Renders the most recent info on the website author
    and allows user collaboration requests
    displays an individual instance of :model: `about.About`.
    **Context**
    ``about``
        The most recent instance of  :model: `about.About`.
    ``form``
        An instance of :form: `about.CollaborateForm`.
    **Template:**
    :template: `about/about.html`.

    """
    template = 'about/about.html'
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == 'POST':
        form = CollaborateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your collaborate is under prosess')
        else:
            messages.add_message(request, messages.ERROR, 'Please check your form')
    else:
        form = CollaborateForm()

    context = {
        'about': about,
        'form': form,
    }
    return render(request, template, context)
