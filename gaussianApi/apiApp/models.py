
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30, blank=True, default='')

	class Meta:
		ordering = ('created',)

class Profile(models.Model):
	user = models.OneToOneField(User)
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30, blank=True, default='')
	surname = models.CharField(max_length=30, blank=True, default='')

class Group(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30, blank=True, default='')
	# members field should be added as a one2many relation between group and user
	isPublic = models.BooleanField(default = True)
	description = models.TextField();
	location_lat = models.CharField(max_length = 10, blank=True)
	location_lon = models.CharField(max_length = 10, blank=True)
	avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
	#tags field should be added as a one2many relation between group and tags

	class Meta:
		ordering = ('created',)

class Comment(models.Model):
	author = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ('created',)

