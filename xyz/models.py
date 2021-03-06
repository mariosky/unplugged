from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Generation(models.Model):
    generation_name = models.CharField(max_length=128)
    generation_number = models.PositiveSmallIntegerField(unique=True)
    next_generation = models.NullBooleanField()
    available_from = models.DateTimeField()
    available_until = models.DateTimeField()

    def __unicode__(self):
        return self.generation_name



class Painting(models.Model):
    title = models.CharField(max_length=128, null=True)
    author = models.ForeignKey(User, null=False)
    published = models.DateTimeField(auto_now=True)
    summary = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='paintings', blank=True)
    generation = models.ForeignKey(Generation, null=True)
    parents = models.ManyToManyField("self",blank=True, null=True)

    def __unicode__(self):
        return self.title


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artists', blank=True)
    bio = models.TextField(blank=True)
    expositions = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username
