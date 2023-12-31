#!/usr/bin/env python3
"""
simple-pagination Module
"""


import csv
import math
from typing import List, Tuple


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """server class to paginate a database of popular baby names.
    """
    DATA_FILE = "popular_baby_names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Pagination method
        """
        assert isinstance(page, int) and page > 0, "Page greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page_size must 0"
        try:
            start_index, end_index = index_range(page, page_size)
            paginated = self.dataset()[start_index:end_index]
        except indexError:
            return []
        return paginated
