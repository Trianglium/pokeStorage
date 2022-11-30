from django.db import models

class Pokemon(models.Model):
    def __init__(self, data):
        self.abilities = data["abilities"]
        self.base_experience = data["base_experience"]
        self.forms = data["forms"]
        self.game_indices = data["game_indices"]
        self.held_items = data["held_items"]
        self.height = data["height"]
        self.held_items = data["held_items"]
        self.id = data["id"]
        self.is_default = data["is_default"]