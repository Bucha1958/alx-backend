#!/usr/bin/env python3
"""
The Module contains helper function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Index_range with two parameters
    page - first parameter
    page_size - second parameter
    It returns a tuple
    """

    offset = (page - 1) * page_size
    limit = offset + page_size - 1
    return (offset, limit)
