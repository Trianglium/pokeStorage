from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from versatileimagefield.fields import VersatileImageField, PPOIField


class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)

    class Meta:
        ordering = ["value"]

    def __str__(self):
        return self.value


class Collection(models.Model):
    name = models.TextField(blank=True)
    pokemon = models.JSONField()

    def __str__(self):
        return self.name
