from django import forms
from .models import redirect_elements

class RedirectForm(forms.ModelForm):
    class Meta:
        model = redirect_elements
        fields = [
            "title",
            "redirect_url",
        ]