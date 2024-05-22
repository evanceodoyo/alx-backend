#!/usr/bin/python3
"""
Module that implements a basic caching system.
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    Defines put and get methods
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item in the cache
        """
        return self.cache_data.get(key)
