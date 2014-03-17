'''
Created on Mar 14, 2014

@author: Andres
'''
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tastypie.utils.timezone import now 
  

class Entry(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)