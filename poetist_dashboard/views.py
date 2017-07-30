from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from poetist_core.models import all_authors, all_poems, all_riddles, all_stories, taggers

# Import forms from core
from poetist_core.forms import PoemForm, RiddleForm, StoryForm

############################### I N D E X ##################################
@user_passes_test(lambda u: u.is_superuser)
def index(request):
	poems = all_poems.objects.all()
	poem_published = all_poems.objects.filter(show_poem = True)
	poem_draft = all_poems.objects.filter(show_poem = False)

	stories = all_stories.objects.all()
	stories_published = all_stories.objects.filter(show_story = True)
	stories_draft = all_stories.objects.filter(show_story = False )

	riddles = all_riddles.objects.all()
	riddles_published = all_riddles.objects.filter(show_riddle = True)
	riddles_draft = all_riddles.objects.filter(show_riddle = False)

	context = {
		"name" : "d_index",

		"poems" : poems,
		"poem_draft" : poem_draft,
		"poem_published" : poem_published,
		
		"stories" : stories,
		"story_draft" : stories_draft,
		"story_published" : stories_published,
		
		"riddles" : riddles,
		"riddle_draft" : riddles_draft,
		"riddle_published" : riddles_published,

		"hide_area_chart" : True,
		"hide_donut" : True,
		"hide_task_panel" : True,
		"hide_transaction_panel" : True,

	}
	
	return render(request, 'poetist_dashboard/dashboard_base.html', context)

############################### P O E M S ##################################

############################### N E W   P O E M
@user_passes_test(lambda u: u.is_superuser)
def new_poem(request):
	form = PoemForm(request.POST or None)
	if form.is_valid():
		
		instance = form.save(commit=False)
		instance.save()
		form.save_m2m()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"tab_text" : "New Poem",
		"head_text" : "Poem!",
		"small_head_text" : "Congratulations on writing a new poem. All the best",
		"breadcrumb_text" : "Writing new Poem",
		"sub_head_text" : "Please fill in all the boxes below",
		"button_text" : "Publish New Poem",
		"form": form,
		"name" : "d_n_poem",
	}
	return render(request, 'poetist_dashboard/form.html', context)

############################### E D I T   P O E M
@user_passes_test(lambda u: u.is_superuser)
def edit_poem(request, slug = None):
	instance = get_object_or_404(all_poems, slug=slug)
	form = PoemForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Poem edited Succesfully")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"tab_text" : "Edit Poem",
		"head_text" : "Poem!",
		"small_head_text" : "This page should load all the contents of this poem. All the best",
		"breadcrumb_text" : "Editing old Poem",
		"sub_head_text" : "Please Edit all the necessary boxes below",
		"button_text" : "Publish Edited",
		"form": form,
		"name" : "d_e_poem",
		"this_poem" : instance,
	}	
	return render(request, 'poetist_dashboard/form.html', context)

############################### A L L   P O E M S
@user_passes_test(lambda u: u.is_superuser)
def all_poem(request):
	cn = "All Poems"
	cnd = "These are the poems published on this site."
	poems = all_poems.objects.all()
	poem_published = all_poems.objects.filter(show_poem = True)
	poem_draft = all_poems.objects.filter(show_poem = False)

	context = {
		"name" : "d_a_poem",
		"content_name" : cn,
		"content_name_detail" : cnd,
		"poems" : poems,
		"poem_draft" : poem_draft,
		"poem_published" : poem_published,
	}
	return render(request, 'poetist_dashboard/d_content_list.html', context)

############################### S T O R I E S ##################################

############################### N E W   S T O R Y 
@user_passes_test(lambda u: u.is_superuser)
def new_story(request):
	form = StoryForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "New Story Published Successfully")
	context = {
		"tab_text" : "New Story",
		"head_text" : "Story Time!",
		"small_head_text" : "Congratulations on completing your new story. All the best",
		"breadcrumb_text" : "Writing a new Story",
		"sub_head_text" : "Please fill in all the boxes below",
		"name" : "d_n_story",
		"form" : form,
		"button_text" : "Publish New"
	}
	
	return render(request, 'poetist_dashboard/form.html', context)

############################### E D I T   S T O R Y 
@user_passes_test(lambda u: u.is_superuser)
def edit_story(request, slug = None):
	instance = get_object_or_404(all_stories, slug = slug)
	form = StoryForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Story edited Successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"tab_text" : "Edit Story",
		"head_text" : "Story time!",
		"small_head_text" : "This page should load all the contents of this story. All the best",
		"breadcrumb_text" : "Editing old Story",
		"sub_head_text" : "Please edit all the necessary box below",
		"button_text" : "Publish Edited",
		"form": form,
		"name" : "d_e_story",
	}
	
	return render(request, 'poetist_dashboard/form.html', context)

############################### A L L   S T O R I E S
@user_passes_test(lambda u: u.is_superuser)
def all_story(request):
	cn = "All Stories"
	cnd = "These are the stories published on this site."
	stories = all_stories.objects.all()
	stories_published = all_stories.objects.filter(show_story = True)
	stories_draft = all_stories.objects.filter(show_story = False )

	context = {
		"name" : "d_a_story",
		"content_name" : cn,
		"content_name_detail" : cnd,
		"stories" : stories,
		"story_draft" : stories_draft,
		"story_published" : stories_published,
	}
	return render(request, 'poetist_dashboard/d_content_list.html', context)


############################### R I D D L E S ##################################

############################### N E W   R I D D L E
@user_passes_test(lambda u: u.is_superuser)
def new_riddle(request):
	form = RiddleForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "New Riddle Published Successfully")
	context = {
		"tab_text" : "New Riddle",
		"head_text" : "Time for a Riddle!",
		"small_head_text" : "Congratulations on making a new riddle. All the best",
		"breadcrumb_text" : "Creating a new Riddle",
		"sub_head_text" : "Please fill in all the boxes below",
		"form" : form,
		"button_text" : "Publish New",
		"name" : "d_n_riddle",
	}
	
	return render(request, 'poetist_dashboard/form.html', context)

############################### E D I T   R I D D L E
@user_passes_test(lambda u: u.is_superuser)
def edit_riddle(request, slug = None):
	instance = get_object_or_404(all_riddles, slug = slug)
	form = RiddleForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Riddle edited Successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"tab_text" : "Edit Riddle",
		"head_text" : "Time for a Riddle!",
		"small_head_text" : "This page should load all the contents of this riddle. All the best",
		"breadcrumb_text" : "Editing old Riddles",
		"sub_head_text" : "Please edit all the necessary boxes below",
		"button_text" : "Publish Edited",
		"form": form,
		"name" : "d_e_riddle",
	}
	
	return render(request, 'poetist_dashboard/form.html', context)

############################### A L L   R I D D L E S
@user_passes_test(lambda u: u.is_superuser)
def all_riddle(request):
	cn = "All Riddles"
	cnd = "These are the riddles published on this site."
	riddles = all_riddles.objects.all()
	riddles_published = all_riddles.objects.filter(show_riddle = True)
	riddles_draft = all_riddles.objects.filter(show_riddle = False)
	context = {
		"name" : "d_a_riddle",
		"content_name" : cn,
		"content_name_detail" : cnd,
		"riddles" : riddles,
		"riddle_draft" : riddles_draft,
		"riddle_published" : riddles_published,
	}
	return render(request, 'poetist_dashboard/d_content_list.html', context)

############################### C H A R T S ##################################
@user_passes_test(lambda u: u.is_superuser)
def charts(request):
	context = {
		"name" : "d_charts",
	}
	
	return render(request, 'poetist_dashboard/charts.html', context)

############################### T A B L E S ##################################
@user_passes_test(lambda u: u.is_superuser)
def tables(request):
	context = {
		"name" : "d_tables",
	}
	
	return render(request, 'poetist_dashboard/tables.html', context)

############################### G U I D E  ##################################
@user_passes_test(lambda u: u.is_superuser)
def guide(request):
	context = {
		"name" : "d_guide",
	}

	return render(request, 'poetist_dashboard/guide.html', context)

