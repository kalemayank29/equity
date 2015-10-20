from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from equity import settings
from django.contrib.auth.decorators import login_required

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def Login(request):
	next = request.GET.get('next', '/home/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user.")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	
	return render(request, "index/login.html", {'redirect to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
	return render(request, "index/home.html", {})

def Mylist(request):
	return render(request, "index/mylist.html", {})

def Stocks(request):
	return render(request, "index/stocks.html", {})
