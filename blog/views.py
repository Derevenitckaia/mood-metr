from django.shortcuts import render

from .models import Estimate_of_day
from .forms import Estimate_of_day_form
from django.contrib.auth.models import User

# Create your views here.
def day_detail_view(request):

	obj = Estimate_of_day.objects.get(id=2)
	context = {
		'date' : obj.date,
		'estimate' : obj.estimate
	}

	return render(request, 'blog/day_detail.html', context)

def all_estimate_view(request):	
	all_objects = Estimate_of_day.objects.filter(user_id = request.user.id)
	context = {
		'days' : all_objects,
		'pays' : Estimate_of_day.objects.all()
	}

	return render(request, 'blog/all_days.html', context)

def estimate_create_view(request):
	form = Estimate_of_day_form(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'form' : form
	}
	return render(request, 'blog/estimate_create.html', context)