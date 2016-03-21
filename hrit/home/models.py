# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models import TextField
from django_markdown.models import MarkdownField

class Content(models.Model):
    text = models.CharField(max_length=200)
    apresentation = MarkdownField(blank=True)
    about = MarkdownField(blank=True)
    def __unicode__(self):
        return self.text

class Member(models.Model):
    name = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200, blank=True)
    apresentation = MarkdownField(blank=True)
    description = MarkdownField(blank=True)
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    def __unicode__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = MarkdownField(blank=True)
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    def __unicode__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    synopsis = models.TextField(blank=True)
    description = MarkdownField(blank=True)
    image = models.FileField(upload_to='documents/%Y/%m/%d')
    def __unicode__(self):
        return self.name
