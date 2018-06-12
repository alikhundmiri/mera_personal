from django.shortcuts import render
from random import randint

from .models import Type_of_Platform, platform, sources
from advertisment.models import ads


def index(request):
	context = {}
	return render(request, 'temp_file.html', context)

def platform_list(request):
	count_ads = ads.objects.count()
	adverts = ads.objects.filter(public_display=True)[randint(0, count_ads - 1)]
	all_platforms = platform.objects.filter(all_sources__public_display=True, public_display=True).distinct()
	context = {
	"all_platforms" : all_platforms,
	"advert" :adverts,
	}
	return render(request, 'platform_list.html', context)