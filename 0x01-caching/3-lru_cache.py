#!/usr/bin/python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherit from BaseCaching """
    def __init__(self):
        super().__init__()
        self.list_aux = []
        self.dict_aux = {}

    def put(self, key, item):
        """ Add LRU """
        if key is None or item is None:
            return
        if key not in self.dict_aux:
            self.dict_aux[key] = 0
        else:
            self.dict_aux[key] += 1
        for i in self.list_aux:
            if i == key:
                self.list_aux.remove(i)
        self.list_aux.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            min_value = min(self.dict_aux.values())
            min_keys = []
            for key in self.dict_aux:
                if self.dict_aux[key] == min_value:
                    min_keys.append(key)

            for i in self.list_aux:
                if i in min_keys:
                    to_remove = i
                    self.list_aux.remove(i)
                    break
            del self.cache_data[to_remove]
            print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """ Get LRU """
        if key is None or key not in self.cache_data:
            return None
        self.dict_aux[key] += 1
        for i in self.list_aux:
            if i == key:
                self.list_aux.remove(i)
        self.list_aux.append(key)
        return self.cache_data[key]
