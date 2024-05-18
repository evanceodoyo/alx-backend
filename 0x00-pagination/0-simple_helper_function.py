#!/usr/bin/env python3
"""
Contains a simple helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    Function that returns of size two containing a start index and end index
    corresponding to the range of indexes to return in a list for those
    particular parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
