from django.shortcuts import render
from .models import events, all_location, bridegroom_list, bride_list

def index(request):
	event_s  = events.objects.all()
	context = {
		"events" : event_s,
	}
	return render(request, 'cereminder/sample.html', context)


def detail(request, id=None):
	event_s  = events.objects.get(id=id)
	context = {
		"event" : event_s,
	}
	return render(request, 'cereminder/detail_invite.html', context)

def whatsnext(request):
	event_s = events.objects.order_by('event_date').all()
	context = {
		"events" : event_s,
	}
	return render(request, 'cereminder/whats_next.html', context)
