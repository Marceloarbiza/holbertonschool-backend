#!/usr/bin/python3
""" 3-main LRU Cache """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LRUCache inherit from BaseCaching """
    list_aux = []
    dict_aux = {}

    def __init__(self):
        """ Init instance BaseCaching """
        super().__init__()

    def put(self, key, item):
        """ Add LRU to cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.dict_aux:
            self.dict_aux[key] = 0
        else:
            self.dict_aux[key] += 1
        for i in self.list_aux:
            if i == key:
                self.list_aux.remove(i)
        self.list_aux.append(key)

        min_value = min(self.dict_aux.values())
        min_keys = []
        for key in self.dict_aux:
            if self.dict_aux[key] == min_value:
                min_keys.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            for i in self.list_aux:
                if i in min_keys:
                    to_remove = i
                    break
            self.list_aux.remove(to_remove)
            del self.cache_data[to_remove]
            del self.dict_aux[to_remove]

            print("DISCARD: {}".format(to_remove))

    def get(self, key):
        """ Get LRU to cache """
        if key is None or key not in self.cache_data:
            return None
        self.dict_aux[key] += 1
        for i in self.list_aux:
            if i == key:
                self.list_aux.remove(i)
        self.list_aux.append(key)
        return self.cache_data[key]
