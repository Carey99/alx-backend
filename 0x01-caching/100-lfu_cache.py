#!/usr/bin/env python3
"""
    LFUCache that inherits from BaseCaching and is a caching system
    You must use self.cache_data - dictionary from the parent class
    You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    def put(self, key, item):
    Must assign to the dictionary
    self.cache_data the item value for the key key.
    if key or item is None, this method should not do anything.
    If the number of items in self.cache_data is
    higher that BaseCaching.MAX_ITEMS:
    you must discard the least frequently used item (LFU algorithm)
    if you find more than 1 item to discard, discard the least recently used
    item
    you must print  DISCARD: with the key discarded and following by a new line
    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key
    doesn’t exist in self.cache_data, return None
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        LFUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
            Init from BaseCaching
        """
        super().__init__()
        self.lfu = []

    def put(self, key, item):
        """
            Must assign to the dictionary
            self.cache_data the item value for the key key.
            if key or item is None, this method should not do anything.
            If the number of items in self.cache_data is
            higher that BaseCaching.MAX_ITEMS:
            you must discard the least frequently used item (LFU algorithm)
            if you find more than 1 item to discard,
            discard the least recently used
            item
            you must print  DISCARD: with the key
            discarded and following by a new line
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discard = self.lfu.pop(0)
                    del self.cache_data[discard]
                    print("DISCARD: {}".format(discard))
                self.cache_data[key] = item
            if key in self.lfu:
                self.lfu.remove(key)
            self.lfu.append(key)

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
            If key is None or if the key
            doesn’t exist in self.cache_data, return None
        """
        if key is not None and key in self.cache_data:
            self.lfu.remove(key)
            self.lfu.append(key)
            return self.cache_data[key]
        return None
