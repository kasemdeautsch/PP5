from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# Create your views here.

def profile(request):
    """
    Displays the user's profile
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'user_profile': user_profile,

    }

    return render(request, template, context)