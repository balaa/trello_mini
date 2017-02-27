from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class AbstractModel(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='%(class)s_updated_by', blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        """ return unicode strings """
        return '%s' % self.name


class Board(AbstractModel):

    pass


class List(AbstractModel):

    pass


class Card(AbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(auto_now=True)
    label = models.CharField(max_length=100)


