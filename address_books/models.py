# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.text

class Entry(models.Model):
    category = models.ForeignKey(Category)
    phone_number = models.CharField(max_length=11)
    name = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name + "    " + self.phone_number


