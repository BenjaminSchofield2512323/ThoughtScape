from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import hashlib

# Create your models here.

class thought(models.Model):
    Options = (
               ('P', 'Public'),
               ('F', 'Friends'),
               ('S', 'Select'),
               )
    content = models.CharField(max_length=140)
    Privacy = models.CharField(max_length=1, choices=Options)
    user = models.ForeignKey(User, related_name="user", primary_key=True)
    creation_date = models.DateTimeField(auto_now=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user1", primary_key=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    
    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#user.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])