from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from versatileimagefield.fields import VersatileImageField, PPOIField

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    #     self.abilities=
    #     self.base_experience=
    #     self.forms=
    #     self.game_indices=
    #     self.height=
    #     self.held_items=
    #     self.id=
    #     self.is_default=
    #     self.location_area_encounters=
    #     self.moves=
    #     self.name=
    #     self.order=
    #     self.past_types=
    #     self.species=
    #     self.sprites=
    #     self.stats=
    #     self.types=
    #     self.weight=
    pass
    hero_image = VersatileImageField(
        upload_to="hero_images", 
        ppoi_field="ppoi", 
        null=True, 
        blank=True
    )
    # https://django-versatileimagefield.readthedocs.io/en/latest/model_integration.html#model-integration
    
    ppoi = PPOIField(null=True, blank=True)
    # https://django-versatileimagefield.readthedocs.io/en/latest/specifying_ppoi.html#the-ppoifield

    def __str__(self):
        return f'{self.number}, {self.name}'
