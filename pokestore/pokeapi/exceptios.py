class PokeApiException(Exception):
    # Base Exception for all exceptions
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
