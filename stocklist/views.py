from django.shortcuts import render
from django.http import HttpResponse
from stocklist.models import Stock

# Create your views here.
def index(request):
    stock_list = Stock.objects.all()
    output = ', '.join([p.tickr for p in stock_list])
    return HttpResponse(output)

    #return HttpResponse("<h1> Welcome to Equity </h1>")
