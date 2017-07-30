from django.shortcuts import render, get_object_or_404, redirect
from .models import all_authors, all_poems, all_riddles, all_stories, taggers, all_about

def about(request):
	name = "about"
	qna = all_about.objects.filter(show_about = True)
	context = {
		"qna"  : qna,
		'name_nav' : name,
		'name' : "About",

	}
	return render(request, 'poetist_about.html', context)

def index(request):
	name = "Writers' Portfolio"
	p_status = True
	r_status = True
	s_status = True


	poems = all_poems.objects.filter(show_poem = True)
	riddles = all_riddles.objects.filter(show_riddle = True)
	stories = all_stories.objects.filter(show_story = True)
	authors = all_authors.objects.all()

	# This two lines below, check if the 'poems' is empty
	if bool(poems) == False:
		p_status = False # if empty, make p_status to False
	
	# This two lines below, check if the 'riddles' is empty
	if bool(riddles) == False:
		r_status = False
	
	# This two lines below, check if the 'stories' is empty
	if bool(stories) == False:
		s_status = False

	context = {
		'name' : name,
		'poems' : poems,
		'riddles' : riddles,
		'stories' : stories,
		'authors' : authors,
		'p_status' : p_status,
		'r_status' : r_status,
		's_status' : s_status,
	}
	return render(request, 'poetist_core/poetist_index.html', context)

def poem_list(request):
	p_status = True

	name = "All Poems"
	poems = all_poems.objects.filter(show_poem = True)
	# This two lines below, check if the 'poems' is empty
	if bool(poems) == False:
		p_status = False # if empty, make p_status to False
	

	context = {
		'name' : name,
		'name_nav' : 'poem',
		'poems' : poems,
		'breadcrumb_text_0' : "All Poems",
		'p_status' : p_status,
	}
	return render(request, 'poetist_core/poetist_list.html', context)


def story_list(request):
	s_status = True
	name = "All Stories"
	stories = all_stories.objects.filter(show_story = True)
	# This two lines below, check if the 'stories' is empty
	if bool(stories) == False:
		s_status = False

	context = {
		'name' : name,
		'name_nav' : 'story',
		'stories' : stories,
		'breadcrumb_text_0' : "All Stories",
		's_status' : s_status,
	}
	return render(request, 'poetist_core/poetist_list.html', context)

def riddle_list(request):
	r_status = True
	name = "All Riddles"
	riddles = all_riddles.objects.filter(show_riddle = True)
	# This two lines below, check if the 'riddles' is empty
	if bool(riddles) == False:
		r_status = False

	context = {
		'name' : name,
		'name_nav' : 'riddle',
		'riddles' : riddles,
		'breadcrumb_text_0' : "All Riddles",
		'r_status' : r_status,		
	}
	return render(request, 'poetist_core/poetist_list.html', context)

def author_list(request):
	name = "All Authors"
	authors = all_authors.objects.all()

	context = {
		'name' : name,
		'name_nav' : 'author',		
		'authors' : authors,
	}
	return render(request, 'poetist_core/poetist_list.html', context)


def poem_detail(request, slug=None):
	name = "Poem"
	poem = get_object_or_404(all_poems, slug = slug)
	# print(poem)
	context = {
		"name" : name,
		'name_nav' : 'poem',		
		"poems" : poem,
		'breadcrumb_text_0' : "All Poems",
		'breadcrumb_text_1' : "All Poems",		
	}
	return render(request, 'poetist_core/poetist_detail.html', context)

def story_detail(request, slug=None):
	name = "Story"
	story = get_object_or_404(all_stories, slug=slug)
	context = {
		"name" : name,
		'name_nav' : 'story',		
		"stories" : story,
		'breadcrumb_text_0' : "All Stories",
		'breadcrumb_text_1' : "All Stories",	
	}
	return render(request, 'poetist_core/poetist_detail.html', context)

def riddle_detail(request, slug=None):
	name = "Riddle"
	riddle = get_object_or_404(all_riddles, slug=slug)
	context = {
		"name" : name,
		'name_nav' : 'riddle',		
		"riddles" : riddle,
		'breadcrumb_text_0' : "All Riddles",
		'breadcrumb_text_1' : "All Riddles",	
	}
	return render(request, 'poetist_core/poetist_detail.html', context)

def author_detail(request, user_name=None):
	name = "Author"
	# author = get_object_or_404(all_authors, user_name__icontain = user_name)
	# print(author)
	author = "Author Detail"
	context = {
		"name" : name,
		'name_nav' : 'author',				
		"authors" : author,
	}
	return render(request, "poetist_core/poetist_detail.html", context)