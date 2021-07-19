import nimporter  # type: ignore
from nim import table

from implementation.py.base import BaseHashTable


class NimTable(BaseHashTable):
    def __init__(self, size: int = 8, max_load_factor: float = 1):
        self.table = table.newTable(size=size, maxLoadFactor=max_load_factor)

    @property
    def load_factor(self):
        return self.table.loadFactor()

    def __setitem__(self, key: int, value: str):
        self.table.setItem(key, value)

    def __getitem__(self, item):
        return self.table.getItem(item)

    def __delitem__(self, key):
        self.table.delItem(key)
