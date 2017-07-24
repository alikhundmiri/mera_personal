from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import  mywork, hosted_projects

# Create your views here.
def first_list(request):
    today = timezone.now().date()
    list_ = mywork.objects.all()
    website_list = mywork.objects.website()
    android_list = mywork.objects.android()
    ios_list = mywork.objects.ios()
    python_list = mywork.objects.python()

    website_hosted = hosted_projects.objects_hosted.website()
    context = {
        "nbar" : "work",
        "websites": website_list,
        "android_apps" : android_list,
        "ios_apps" : ios_list,
        "python" : python_list,
        "websites_hosted": website_hosted,
        "list": list_,
        "today": today,
    }
    return render(request, "first/first_list.html", context)


def first_detail(request, slug = None):
    instance = get_object_or_404(mywork, slug=slug)

    context = {
        "nbar" : "work",
        "type": instance.type_work,
        "instance": instance,
    }
    return render(request, "first/first_detail.html", context)


def hosted_detail(request, slug = None):
    instance = get_object_or_404(hosted_projects, slug=slug)

    context = {
        "nbar" : "work",
        "type": instance.type_work,
        "instance": instance,
    }
    return render(request, "first/first_hosted.html", context)    