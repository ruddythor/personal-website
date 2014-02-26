from django.db import models
from django.contrib.auth.models import User
from arenafighter.utils import dice
from arenafighter.models.equipment import Inventory, InventoryItem, Armor, Weapon



class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    class Meta:
        app_label = 'arenafighter'

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)


