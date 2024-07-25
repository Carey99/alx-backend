#!/usr/bin/env python3
"""
    MRUCache inherits from BaseCaching and is a caching system
    must use self.cache_data - dictionary from the parent class
    can overwrite def __init__(self):
    but don’t forget to call the parent super().__init__(self)
    def put(self, key, item):
    must assign to the dictionary self.cache_data
    the item value for the key key.
    if the number of items in self.cache_data is higher
    that BaseCaching.MAX_ITEMS:
    must discard the most recently used item (MRU algorithm)
    must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
    must return the value in self.cache_data linked to key.
    if key is None or if the key doesn’t exist in self.cache_data
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
        MRUCache class
    """
    def __init__(self):
        """
            Initializer
        """
        super().__init__()

    def put(self, key, item):
        """
            Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = list(self.cache_data.keys())[-1]
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item

    def get(self, key):
        """
            Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
