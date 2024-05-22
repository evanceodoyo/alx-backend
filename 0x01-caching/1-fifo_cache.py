#!/usr/bin/python3
"""
Implements a simple FIFO cache.
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines methods for simple FIFO caching system.
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

        keys = list(self.cache_data.keys())
        if len(keys) > BaseCaching.MAX_ITEMS:
            del self.cache_data[keys[0]]
            print(f"DISCARD: {keys[0]}")

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
