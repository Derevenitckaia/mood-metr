from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def home_page(request):
	if User.is_anonymous:
		return render(request, 'core/home_page.html')
	else:
		return redirect('all_days')
