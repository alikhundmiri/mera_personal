from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import tweeting


@user_passes_test(lambda u: u.is_superuser)
def tweetlist(request):
	today = timezone.now().date()
	tweets = tweeting.objects.all()
	query = request.GET.get("q")
	if query:
		tweets = tweets.filter(
			Q(title__icontains=query)|
			Q(detail__icontains=query)
		).distinct()

	paginator = Paginator(tweets, 30) # show 30 Blogs per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		all_tweets = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		all_tweets = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		all_tweets = paginator.page(paginator.num_pages)



	context = {
		"tweets" : tweets,
		"all_tweets" : all_tweets,
		"today" : today,
		"title" : "Tweets",
		"page_request_var" : page_request_var,
	
	}

	return render(request, "tweetme/tweetslist.html", context)


@user_passes_test(lambda u: u.is_superuser)
def tweet_detail(request, id=None):
	today = timezone.now().date()
	this_tweet = get_object_or_404(tweeting, id = id)
	tweet_percent = (len(this_tweet.tweet)/140)*100
	print(tweet_percent)
	context = {
		"tweet" : this_tweet,
		"tweet_percent" : tweet_percent,

	}
	return render(request, "tweetme/tweet_detail.html", context)

@user_passes_test(lambda u: u.is_superuser)
def tweet_update(request, id=None):
	context = {
	
	}
	return render(request, "tweetme/tweet_update.html", context)
	
@user_passes_test(lambda u: u.is_superuser)
def tweet_delete(request, id=None):
	instance = get_object_or_404(tweeting, id=id)
	if instance.user != request.user:
		raise Http404
	instance.delete()
	messages.success(request, "tweet deleted Successfully!!")
	return redirect("tweetme:list")
	
