from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from equity import settings
from django.contrib.auth.decorators import login_required
from stocklist.models import Stock
from stocklist.models import Pick

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")


def get_tickr(request):
	if request.method == 'POST':
		tickr_name = request.POST['tickr_name']
		if tickr_name == "":
			return HttpResponse("Please enter a TICKR!")
		else:
			return Stockinfo(request, tickr_name)
	else:
		return render(request, "index/mylist.html", {})

def add_stock(request):
	tickr_name = request.POST['tickr_name']
	stock = Stock.objects.get(tickr = tickr_name)
	x = Pick(uid=4,tickr=tickr_name,price=stock.price,date=102)
	x.save()
	return HttpResponseRedirect('/picks')

def delete_stock(request):
	tickr_name = request.POST['dtickr_name']
	p = Pick.objects.all()
	for obj in p:
		obj.delete()
	return HttpResponseRedirect('/picks')


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
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index/login.html", {'redirect_to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
	return render(request, "index/home.html", {})

def Mylist(request):
	return render(request, "index/mylist.html", {})

def Stockinfo(request, tickr_name):
	return render(request, "index/stock.html", {'tickr_name' : tickr_name})
