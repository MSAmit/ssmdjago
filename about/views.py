from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "about/about.html")

def contact(request):
	return render(request, "about/basic.html", {'content': ['srisaimotors@gmail.com','0987654321']})
