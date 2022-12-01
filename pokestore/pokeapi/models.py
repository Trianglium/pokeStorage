

# {"ability":{"name":"synchronize","url":"https://pokeapi.co/api/v2/ability/28/"},"is_hidden":false,"slot":1}
class Ability():
    def __init__(self, data):
        self.name = data["name"]
        self.url = data["url"]
        self.is_hidden = data["is_hidden"]
        self.slot = data["slot"]