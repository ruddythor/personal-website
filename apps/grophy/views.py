from django.shortcuts import render

# Create your views here.


def home(request):
	grophy_name = 'GROPHY!'
	context = {'grophy_name': grophy_name}
	return render(request, 'grophyhome.html', context)

def about(request):
	grophy_name = 'GROPHY!'
	context = {'grophy_name': grophy_name}
	return render(request, 'grophy/about.html', context)

def portfolio(request):
	grophy_name = 'GROPHY!'
	context = {'grophy_name': grophy_name}
	return render(request, 'grophyhome.html', context)

def resume(request):
	grophy_name = 'GROPHY!'
	context = {'grophy_name': grophy_name}
	return render(request, 'grophyhome.html', context)

def blog(request):
	grophy_name = 'GROPHY!'
	context = {'grophy_name': grophy_name}
	return render(request, 'grophyhome.html', context)

def videos(request):
	grophy_name = 'GROPHY!'
	context = {'grophy_name': grophy_name}
	return render(request, 'grophyhome.html', context)