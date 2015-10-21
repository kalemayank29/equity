
from stocklist.models import Stock
from stocklist.models import Pick
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from equity import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    stock_list = Stock.objects.all()
    #output = ', '.join([p.tickr for p in stock_list])
    #return HttpResponse(output)
    context = {'stock_list': stock_list}
    return render(request, 'stocks.html', context)

    #return HttpResponse("<h1> Welcome to Equity </h1>"
def picks(request):
    pick_list = Pick.objects.all()
    #output = ', '.join([p.tickr for p in pick_list])
    #return HttpResponse(output)
    context = {'pick_list': pick_list}
    return render(request, 'list.html', context)

def refresh(request):
    stock_list = Stock.objects.all()
    for tup in stock_list:
        tup.price += 1
        tup.save()
    #output = ', '.join([p.tickr for p in pick_list])
    #return HttpResponse(output)
    context = {'stock_list': stock_list}
    return render(request, 'stocks.html', context)
