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
	videocompositing = PortfolioItem.objects.filter(portfolio_item_type='videocompositing')
	context = {'portfolio_items': videocompositing}
	return render(request, 'grophy/portfolio-item-list.html', context)

def photography(request):
	photography = PortfolioItem.objects.filter(portfolio_item_type='photography')
	context = {'portfolio_items': photography}
	return render(request, 'grophy/portfolio-item-list.html', context)

def short_film(request):
	shortfilm = PortfolioItem.objects.filter(portfolio_item_type='shortfilim')
	context = {'portfolio_items': shortfilm}
	return render(request, 'grophy/portfolio-item-list.html', context)


def illustration(request):
	illustrations = PortfolioItem.objects.filter(portfolio_item_type='illustration')
	context = {'portfolio_items': illustrations}
	return render(request, 'grophy/portfolio-item-list.html', context)


def logo_design(request):
	logodesign = PortfolioItem.objects.filter(portfolio_item_type='logodesign')
	context = {'portfolio_items': logodesign}
	return render(request, 'grophy/portfolio-item-list.html', context)

def character_design(request):
	characterdesign = PortfolioItem.objects.filter(portfolio_item_type='characterdesign')
	context = {'portfolio_items': characterdesign}
	return render(request, 'grophy/portfolio-item-list.html', context)

def user_experience(request):
	userexperience = PortfolioItem.objects.filter(portfolio_item_type='userexperience')
	context = {'portfolio_items': userexperience}
	return render(request, 'grophy/portfolio-item-list.html', context)

def painting(request):
	painting = PortfolioItem.objects.filter(portfolio_item_type='painting')
	context = {'portfolio_items': painting}
	return render(request, 'grophy/portfolio-item-list.html', context)

def drawing(request):
	drawing = PortfolioItem.objects.filter(portfolio_item_type='drawing')
	context = {'portfolio_items': drawing}
	return render(request, 'grophy/portfolio-item-list.html', context)

def two_d(request):
	twod = PortfolioItem.objects.filter(portfolio_item_type='twod')
	context = {'portfolio_items': twod}
	return render(request, 'grophy/portfolio-item-list.html', context)

def three_d(request):
	threed = PortfolioItem.objects.filter(portfolio_item_type='threed')
	context = {'portfolio_items': threed}
	return render(request, 'grophy/portfolio-item-list.html', context)
