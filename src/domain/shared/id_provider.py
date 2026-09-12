# domain/shared/id_provider.py

from uuid import uuid4


class IdProvider:

    def generate(self):
        return uuid4()


class FixedIdProvider(IdProvider):

    def __init__(self):
        self.counter = 0

    def generate(self):
        self.counter += 1
        return f"fixed-id-{self.counter}"