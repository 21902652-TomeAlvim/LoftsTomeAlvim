from django.shortcuts import render

def loft_home(request):
	return render(request, 'loft/home.html')