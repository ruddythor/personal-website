from django.db import models
from django.contrib.auth.models import User
from arenafighter.utils import dice
from arenafighter.models.equipment import Inventory, InventoryItem, Armor, Weapon



class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    class Meta:
        app_label = 'arenafighter'

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)


# This is a bit of a hack, but a sexy one, found here
# http://www.turnkeylinux.org/blog/django-profile
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

