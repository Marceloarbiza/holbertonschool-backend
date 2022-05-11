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
        self.list_aux.append((key, self.dict_aux[key]))
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            new_list = sorted(self.list_aux, key=lambda tup: tup[1])
            del self.cache_data[new_list[0][0]]
            print("DISCARD: {}".format(new_list[0][0]))

    def get(self, key):
        """ Get LRU """
        if key is None or key not in self.cache_data:
            return None
        self.dict_aux[key] += 1
        self.list_aux.append((key, self.dict_aux[key]))
        return self.cache_data[key]
