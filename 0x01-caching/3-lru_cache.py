#!/usr/bin/env python3
"""
    LRUCache inherits from BaseCaching
    and is a caching system
    you must use self.cache_data - dictionary from the parent class
    you can overload def __init__(self):
    but don’t forget to call the parent init super().__init__()
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the
    item value for the key key.
    If the number of items in self.cache_data is
    higher that BaseCaching.MAX_ITEMS:
    must discard the least accessed item (LRU algorithm)
    You must print the following string once the item is removed:
    DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or
    if the key doesn’t exist in self.cache_data, return None
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        LRU cache system
    """

    def __init__(self):
        """
            Initiliaze
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
            Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """
            Get an item by key
        """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
