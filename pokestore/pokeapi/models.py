
# abilities
# {"ability":{"name":"synchronize","url":"https://pokeapi.co/api/v2/ability/28/"},"is_hidden":false,"slot":1}
class Ability():
    def __init__(self, data):
        self.name = data["name"]
        self.url = data["url"]
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]


# base_experience

# forms
class Form():
    def __init__(self, data):
        self.name = data["name"]
# game_indices
class GameIndice():
    def __init__(self, data):
        self.name = data["name"]
# height
# held_items
class Item():
    def __init__(self):
        pass
# id
# is_default
# location_area_encounters
class LocationArea():
    def __init__(self):
        pass
# moves
class Move():
    def __init__(self):
        pass
