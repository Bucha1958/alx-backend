#!/usr/bin/env python3
"""hypermedia pagination module"""


import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary containing given key value pairs"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if data == []:
            page_size = 0
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None

        dct = {"page_size": page_size,
               "page": page,
               "data": data,
               "next_page": next_page,
               "prev_page": prev_page,
               "total_pages": total_pages}
        return dct
