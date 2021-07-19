from abc import abstractmethod


class BaseNode:
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def add_value(self, key, value):
        ...

    @abstractmethod
    def remove_value(self, key):
        ...

    @abstractmethod
    def get_value(self, key):
        ...


class BaseHashTable:
    @abstractmethod
    def __init__(self, size, max_load_factor):
        ...

    @property
    @abstractmethod
    def load_factor(self):
        ...

    @abstractmethod
    def __setitem__(self, key, value):
        ...

    @abstractmethod
    def __getitem__(self, item):
        ...

    @abstractmethod
    def __delitem__(self, key):
        ...
