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