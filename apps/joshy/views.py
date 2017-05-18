from django.shortcuts import render

# Create your views here.


def home(request):
	joshy_name = 'joshy!'
	context = {'grophy_name': joshy_name}
	return render(request, 'joshyhome.html', context)