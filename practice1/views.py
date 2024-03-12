from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def home(request):
    d={
        'lst':['python','is','fun'], "date":datetime.now(),"empty":'',
        'num':5,
        'numlist':[1,2,3,4],
        
    }
    return render (request, 'index.html',d)