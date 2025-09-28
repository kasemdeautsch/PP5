from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form to render in the template and handle collaborate requests

    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
