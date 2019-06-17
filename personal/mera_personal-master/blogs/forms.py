from django import forms
from .models import Post, taggers
from pagedown.widgets import PagedownWidget

class BlogForm(forms.ModelForm):
    detail = forms.CharField(widget=PagedownWidget(show_preview=True))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    # tags = forms.ModelMultipleChoiceField(queryset = taggers.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Post
        fields = [
            "title",
            "detail",
            "image",
            "draft",
            "publish",
            # "tags"
        ]