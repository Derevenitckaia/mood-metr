from django.shortcuts import render, redirect

from .models import Estimate_of_day
from .forms import Estimate_of_day_form
from django.contrib.auth.models import User
import plotly.express as px
from django.contrib import messages

# Create your views here.
def day_detail_view(request):

	obj = Estimate_of_day.objects.get(id=2)
	context = {
		'date' : obj.date,
		'estimate' : obj.estimate
	}

	return render(request, 'blog/day_detail.html', context)

def all_estimate_view(request):	
	all_objects = Estimate_of_day.objects.filter(user_id = request.user.id).order_by('date')
	print('+++',len(all_objects))

	if len(all_objects) != 0 :
		fig = px.line( x = [obj.date for obj in all_objects], 
					y = [obj.estimate for obj in all_objects])
		
		chart = fig.to_html()
	
		context = {
			'days' : all_objects,
			'chart' : chart
		}

		return render(request, 'blog/all_days.html', context)
	else:
		messages.success(request, ('Создайте хотя-бы две оценки, чтобы посмотреть график'))
		return redirect('create_estimate')

def estimate_create_view(request):
	
	form = Estimate_of_day_form(request.POST or None)
	
	if form.is_valid():
		Estimate_of_day = form.save(commit = False)
		Estimate_of_day.user = request.user
		Estimate_of_day.save()
		messages.success(request, ('Оценка создана'))
	context = {
		'form' : form
	}
	
	return render(request, 'blog/estimate_create.html', context)

def delete_estimate(request, estimate_id):
	estimate = Estimate_of_day.objects.get(pk=estimate_id)
	estimate.delete()
	return redirect('all_days')