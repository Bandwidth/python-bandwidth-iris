#!/usr/bin/env python

from iris_sdk.config import Config

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]

class Client(metaclass=Singleton):

    """Controller."""

    def __init__(
            self, account_id=None, username=None, password=None,
            filename=None):

        self._config = Config(account_id, username, password, filename)

    @property
    def config(self):
        return self._config