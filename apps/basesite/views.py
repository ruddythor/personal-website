from django.shortcuts import render

# Create your views here.



def home(request):
	context = {'characters': 'weoijwefoij'}
	return render(request, 'sitehome.html', context)
