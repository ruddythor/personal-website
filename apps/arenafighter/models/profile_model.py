from django.db import models
from django.contrib.auth.models import User
from arenafighter.utils import dice
from arenafighter.models.inventory import Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.character import Character



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    current_character = models.ForeignKey(Character, related_name='profile', null=True)
    class Meta:
        app_label = 'arenafighter'

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)


# This is a bit of a hack, but a sexy one, found here
# http://www.turnkeylinux.org/blog/django-profile
User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

