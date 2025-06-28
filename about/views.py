from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


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
            messages.add_message(request, messages.SUCCESS,
                                 'Thank you for your collaboration, '
                                 'we will take your message in consideration ')
        else:
            messages.add_message(request, messages.ERROR,
                                 'There are some issues with the form, '
                                 'Please check the validation under fields!')
    else:
        form = CollaborateForm()

    context = {
        'about': about,
        'form': form,
    }
    return render(request, template, context)
