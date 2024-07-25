#!/usr/bin/env python3
"""
    BasicCache inherits from BaseCaching
    and is a caching system
    must use self.cache_data - dictionary from the parent class
    no limit on cache size
    method put: must assign to the dictionary self.cache_data
    the item key from the argument key and the value from the argument item
    method get: must return the value in self.cache_data linked to key
    if key is None or if the key doesn't exist in self.cache_data, return None
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        BasicCache class
    """

    def put(self, key, item):
        """
            Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
