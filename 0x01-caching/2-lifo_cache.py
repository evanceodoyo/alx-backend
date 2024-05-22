#!/usr/bin/python3
"""
Implements a simple LIFO cache.
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    Defines methods for simple LIFO caching system.
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if not self.cache_data.get(key):
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")

        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, True)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
