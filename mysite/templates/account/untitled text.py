from django.http import HttpResponse
from __future__ import unicode_literals
from django.apps import apps

from django.contrib.auth.models import User

class user:
	def __init__(self, username, email, password)
		self.u = username
		self.e = email
		self.p = password
	User.objects.create_user('usernane','email','password')