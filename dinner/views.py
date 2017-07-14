from django.shortcuts import render,get_object_or_404

from .models import dishes, meal
from .forms import RandomForm

def show_dishes(request):
	all_dishes = dishes.objects.all()
	all_meals = meal.objects.all()

	query = request.GET.get("q")
	if query:
		print(query)
		suggestion = randomisor(query, all_dishes)

	# print(all_dishes)
	# print(all_meals)
	context = {
		"name" : "Dinner recommendations",
		"d" : all_dishes,
		"m" : all_meals,
		"suggest" : suggestion
	}
	return render(request, "dinner/dinner_index.html", context)

def randomisor(query, all_dishes):
	for food in all_dishes:
		if query in food.meal_type.all():
			print("got one : " + food)
	
	return "related_dishes"


