from django.shortcuts import render
from .models import *
def loft_home(request):
	return render(request, 'loft/home.html', {'lofts': Loft.objects.all()})