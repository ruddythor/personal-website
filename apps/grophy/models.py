from django.db import models

# Create your models here.


class PortfolioItem(models.Model):
	portfolio_item_type = models.TextField(default='')
	portfolio_item = models.FileField()