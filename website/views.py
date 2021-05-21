#  hello/views.py
import datetime
from django.shortcuts import render

def home_page_view(request):
	context = {'time' : datetime.datetime.now()}
	return render(request, 'website/home.html', context)

