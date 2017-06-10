from django.shortcuts import render
from django.http import HttpResponseRedirect,  HttpResponse 
import json, collections
# Create your views here.


def index(request):
	return render(request, "home.html")