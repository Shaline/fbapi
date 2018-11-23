# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    facebook_id = models.TextField()


class FacebookPage(models.Model):
    access_token = models.TextField()
    original_id = models.TextField() # Graph id


class FacebookLabel(models.Model):
    owner = models.ForeignKey(User)
    page = models.ForeignKey(FacebookPage)
    label_id = models.TextField()
