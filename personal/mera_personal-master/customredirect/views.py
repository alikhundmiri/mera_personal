from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from .models import redirect_elements
from .forms import RedirectForm

# Create your views here.
def redirect_intro(request):
	all_links = redirect_elements.objects.all()
	context = {
		'all_links' : all_links,
	}
	return render(request, "customredirect/redirect_intro.html", context)


def redirect_link(request, slug=None):
	# find the link from database, if link doesnt exist, we will see that later
	this_link = get_object_or_404(redirect_elements, slug=slug)

	if this_link:
		this_link.count += 1
		this_link.save()

	context = {
	}
	return HttpResponseRedirect(this_link.redirect_url)

@user_passes_test(lambda u: u.is_superuser)
def redirect_new(request):
	if request.user.is_superuser:
		pass
	else:
		raise Http404

	form = RedirectForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		# instance.user = request.user
		instance.save()
		return HttpResponseRedirect(reverse('customredirect:redirect_intro'))

	context = {
		"form": form,
		"tab_text": "Send Request",
		"top_text": "New Redirect!",
		"form_text": "Here you can create a new redirect link, make sure don't have conflicting link titles.",
		}
	return render(request, 'customredirect/new_link.html', context)

# def blog_create(request):
#     form = BlogForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         # instance.user = request.user
#         instance.save()
#         messages.success(request, "Successfully Created")
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         "nbar" : "blog",
#         "form": form,
#         "tab_text": "New Blog Post",
#         "top_text": "New Blog!",
#         "form_text": "Here you can write your blog using the tools provided below.",
#     }
#     return render(request, 'general_form.html', context)
