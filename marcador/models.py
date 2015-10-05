from django.db import models

# Create your models here.
# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

class PublicBookmarkManager(models.Manager):
	def get_queryset(self):
		qs = super(PublicBookmarkManager, self).get_queryset()
		return qs.filter(is_public=True)

@python_2_unicode_compatible
class Bookmark(models.Model):
	url = models.URLField()
	title = models.CharField('title', max_length=255)
	description = models.TextField('description', blank=True)
	is_public = models.BooleanField('public', default=True)
	date_created = models.DateTimeField('date created')
	date_updated = models.DateTimeField('date updated')
	owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
	tags = models.ManyToManyField(Tag, blank=True)

	class Meta:
		verbose_name = 'bookmark'
		verbose_name_plural = 'bookmarks'
		ordering = ['-date_created']

	def __str__(self):
		return '%s (%s)' % (self.title, self.url)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
			self.date_updated = now()
		super(Bookmark, self).save(*args, **kwargs)
