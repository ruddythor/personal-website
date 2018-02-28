from django.shortcuts import render
from grophy.models import PortfolioItem

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

def video_compositing(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def photography(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def short_film(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)


def illustration(request):
	illustrations = PortfolioItem.objects.filter(portfolio_item_type='image')
	context = {'portfolio_items': illustrations}
	return render(request, 'grophy/portfolio-item-list.html', context)


def logo_design(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def character_design(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def user_experience(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def painting(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def drawing(request):

	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def two_d(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)

def three_d(request):
	context = {}
	return render(request, 'grophy/portfolio-item-list.html', context)
