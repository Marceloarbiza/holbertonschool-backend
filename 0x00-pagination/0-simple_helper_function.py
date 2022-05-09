#!/usr/bin/env python3
"""
The function should return a tuple of size two
containing a start index and an end index
"""


def index_range(page, page_size):
    """
    Function that returns the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)
