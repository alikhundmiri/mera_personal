from django.conf.urls import url, include
from . import views
from poetist_dashboard import views as d_views

urlpatterns = [
	url(r'^$', views.index, name='list'),

	url(r'^riddles$', views.riddle_list, name='riddle_list'),
	url(r'^stories$', views.story_list, name='story_list'),
	url(r'^poems$', views.poem_list, name='poem_list'),
	url(r'^authors$', views.author_list, name='author_list'),
	
	
	url(r'^poems/(?P<slug>[\w-]+)$', views.poem_detail, name='poem_detail'),
	url(r'^stories/(?P<slug>[\w-]+)$', views.story_detail, name='story_detail'),
	url(r'^riddles/(?P<slug>[\w-]+)$', views.riddle_detail, name='riddle_detail'),
	
	url(r'^poems/(?P<slug>[\w-]+)/edit', d_views.edit_poem, name='edit_poem'),
	url(r'^stories/(?P<slug>[\w-]+)/edit', d_views.edit_story, name='edit_story'),
	url(r'^riddles/(?P<slug>[\w-]+)/edit', d_views.edit_riddle, name='edit_riddle'),
]
