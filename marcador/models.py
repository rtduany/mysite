from django.db import models

# Create your models here.
# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)


