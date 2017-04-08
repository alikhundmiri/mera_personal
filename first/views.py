from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import  mywork

# Create your views here.
def first_list(request):
    today = timezone.now().date()
    list = mywork.objects.all()
    website_list = mywork.objects.website()
    android_list = mywork.objects.android()
    ios_list = mywork.objects.ios()
    context = {
        "websites": website_list,
        "android_apps" : android_list,
        "ios_apps" : ios_list,
        "list": list,
        "today": today,
    }
    return render(request, "first/first_list.html", context)


def first_detail(request, slug = None):
    instance = get_object_or_404(mywork, slug=slug)

    context = {
        "type": instance.type_work,
        "instance": instance,
    }
    return render(request, "first/first_detail.html", context)