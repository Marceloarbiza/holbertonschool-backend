#!/usr/bin/env python3
"""
The function should return a tuple of size two
containing a start index and an end index
"""


import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


def index_range(page, page_size):
    """
    Function that returns the range of indexes
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of the dataset"""

        assert isinstance(page, int), "AssertionError raised when page \
                                    and/or page_size are not ints"
        assert isinstance(page_size, int), "AssertionError raised when page \
                                    and/or page_size are not ints"
        assert page > 0, "AssertionError raised with negative values"
        assert page_size > 0, "AssertionError raised with negative values"

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]
