from django.db import models

# Create your models here.


class PortfolioItem(models.Model):
	ITEM_TYPE_CHOICES = (
		('image', 'Image'),
		('illustration', 'Illustration'),
		('logodesign', 'Logo Design'),
		('characterdesign', 'Character Design'),
		('userexperience', 'User Experience'),
		('painting', 'Painting'),
		('drawing', 'Drawing'),
		('twod', 'Two D'),
		('threed', 'Three D'),
		('shortfilm', 'Short Film'),
		('photography', 'Photography'),
		('videocompositing', 'Video Compositing')
	)
	portfolio_item_type = models.CharField(max_length=100, choices=ITEM_TYPE_CHOICES)
	portfolio_item = models.FileField()

	def __str__(self):
		return self.portfolio_item.url