from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

from .models import *

def registerPage(request):
	form = UserCreationForm()

	print(request.method)

	if request.method == 'POST':
		print(request.POST)
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save() 
			return redirect('login')
			

	context = {'form' : form}
	return render(request, 'accounts/register.html', context)

def loginPage(request):

	form = AuthenticationForm()
	
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			
		


	context = {'form' : form}
	return render(request, 'accounts/login.html', context)

def logout_user(request):
	messages.success(request, ('You were logged out'))
	logout(request)
	return redirect('home')