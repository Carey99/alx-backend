#!/usr/bin/env python3
"""
   FIFOCache inheriting from BaseCaching
   must use self.cache_data - dictionary from the parent class
   you can overload def __init__(self):
   but don’t forget to call the parent init super().__init__(self)
   def put(self, key, item):
   Must assign to the dictionary self.cache_data
   the item value for the key key.
   If the number of items in self.cache_data is higher
   that BaseCaching.MAX_ITEMS:
   you must discard the first item put in cache (FIFO algorithm)
   you must print DISCARD: with the key discarded and following by a new line
   def get(self, key):
   Must return the value in self.cache_data linked to key.
   If key is None or if the key doesn’t exist in self.cache_data,
   return None
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """

    def __init__(self):
        """
        constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        add to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            first = keys[0]
            self.cache_data.pop(first)
            print("DISCARD: {}".format(first))
        self.cache_data[key] = item

    def get(self, key):
        """
        get from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
