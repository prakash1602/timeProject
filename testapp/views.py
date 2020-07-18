from django.shortcuts import render
from django.http.response import HttpResponse
import datetime as op

def dateview(request):
    d=op.datetime.now()
    x="<h1>the current date and time is{}</h1>".format(d)
    
    return HttpResponse(x)




