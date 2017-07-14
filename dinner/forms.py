from django import forms
from .models import meal, dishes
from pagedown.widgets import PagedownWidget

class RandomForm(forms.Form):
	meal_type = forms.ModelChoiceField(queryset=meal.objects.all())
	class Meta:
		model = meal
		fields = [
			"meal_type",
			"name",
			"timestamp"
		]