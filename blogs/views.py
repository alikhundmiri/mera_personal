from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Post, taggers
from .forms import BlogForm

@login_required
def blog_create(request):
    if request.user.is_superuser:# or not request.user.is_staff or not request.user.is_superuser:
        pass
    else:
        raise Http404
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "nbar" : "blog",
        "form": form,
        "tab_text": "New Blog Post",
        "top_text": "New Blog!",
        "form_text": "Here you can write your blog using the tools provided below.",
    }
    return render(request, 'general_form.html', context)

def blog_detail(request, slug=None):
    today = timezone.now().date()
    this_blog = get_object_or_404(Post, slug = slug)
    if this_blog.draft or this_blog.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "nbar" : "blog",
        "this_blog" : this_blog,
        "today" : today,
    }
    return render(request, "blogs/blog_detail.html", context)


def blog_list(request):
    today = timezone.now().date()
    all_tags = taggers.objects.all()
    posting_privilage = False
    all_blogs_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        all_blogs_list = Post.objects.all()
        posting_privilage = True
    query = request.GET.get("q")
    if query:
        all_blogs_list = all_blogs_list.filter(
            Q(title__icontains=query)|
            Q(detail__icontains=query)
        ).distinct()

    paginator = Paginator(all_blogs_list, 10) # show 10 Blogs per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        all_blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_blogs = paginator.page(paginator.num_pages)
    context = {
        "nbar" : "blog",
        'all_blogs' : all_blogs,
        'all_tags' : all_tags,
        "title" : "Blogs",
        "page_request_var" : page_request_var,
        "posting_privilage" : posting_privilage,
        "today" : today
    }
    return render(request, "blogs/blog_index.html", context)

def blog_archive(request):
    today = timezone.now().date()
    all_tags = taggers.objects.all()
    posting_privilage = False
    all_blogs_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        all_blogs_list = Post.objects.all()
        posting_privilage = True
    query = request.GET.get("q")
    if query:
        all_blogs_list = all_blogs_list.filter(
            Q(title__icontains=query)|
            Q(detail__icontains=query)
        ).distinct()

    paginator = Paginator(all_blogs_list, 100) # show 100 Blogs per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        all_blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_blogs = paginator.page(paginator.num_pages)
    context = {
        "nbar" : "blog",
        'all_blogs' : all_blogs,
        'all_tags' : all_tags,
        "title" : "Blogs",
        "page_request_var" : page_request_var,
        "posting_privilage" : posting_privilage,
        "today" : today
    }
    return render(request, "blogs/blog_archive.html", context)

@login_required
def blog_update(request, slug= None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.user != request.user:
        raise Http404
    form = BlogForm(request.POST or None, request.FILES or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Blog Edited Successfully!!")
        return  HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "nbar" : "blog",
        "form":form,
        "tab_text": "Edit Blog Post",
        "top_text": "Editing tools",
        "form_text": "You can make changes to the blog here!",
        'this_blog': instance,
    }
    return render(request, "general_form.html", context)

@login_required
def blog_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.user != request.user:
        raise Http404
    instance.delete()
    messages.success(request, "Blog deleted Successfully!!")
    return redirect("blogs:list")


def blog_all_tag(request):
    all_tags = taggers.objects.all()
    context = {
        "all_tags" : all_tags,
        "nbar" : "blog",
        }
    return render(request, "blogs/all_tags.html", context)


def blog_tag(request, slug=None):
    all_content = Post.objects.all()
    this_tag = get_object_or_404(taggers, tag_slug=slug)
    print(this_tag)
    print(all_content)
    required_blogs = []
    for content in all_content:
        if this_tag in content.tags.all():
            required_blogs.append(content)
    print(required_blogs)

    context = {
        "this_tag" : this_tag,
        "required_blogs" : required_blogs,
        "nbar" : "blog",
        }
    return render(request, "blogs/content_tag.html", context)
