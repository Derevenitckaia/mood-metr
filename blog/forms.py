from django import forms

from .models import Estimate_of_day

class DateInput(forms.DateInput):
	input_type = 'date'

class Estimate_of_day_form(forms.ModelForm):
	class Meta:
		model = Estimate_of_day
		fields = [
			'date',
			'estimate'
			]
		widgets = {
			'date' : DateInput
		}