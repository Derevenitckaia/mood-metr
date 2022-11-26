from django import forms

from .models import Estimate_of_day

class Estimate_of_day_form(forms.ModelForm):
	class Meta:
		model = Estimate_of_day
		fields = [
			'date',
			'estimate'
			]