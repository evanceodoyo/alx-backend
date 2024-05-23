#!/usr/bin/env python3
"""
Implements Most Recently Used (MRU) cache.
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    Defines methods for MRU caching system.
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache.
        Discard the most recently used item (MRU algorithm)
        """
        if not self.cache_data.get(key):
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {mru_key}")

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if self.cache_data.get(key):
            self.cache_data.move_to_end(key, True)
        return self.cache_data.get(key)
