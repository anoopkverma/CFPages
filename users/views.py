from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserForm
from CFPages.views import home
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])
		user.save()
		return redirect('/')
	else:
		form = UserForm()
		return render(request,'users/register.html',{'form':form})


def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return home(request)
			else:
				return render(request, "users/login.html", {'message':'Account has been disabled!'})
		else:
			return render(request, "users/login.html", {'message':'Invalid username or password !!'})
	else:
		return render(request, "users/login.html", {})

def logout_view(request):
	logout(request)
	return home(request)
