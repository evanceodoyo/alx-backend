#!/usr/bin/env python3
"""
Implementation of a simple pagination.
"""
import csv
from typing import List
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
        """
        Gets the page with items of the given size.
        """
        try:
            assert type(page) is int and\
                page > 0 and\
                type(page_size) is int and\
                page_size > 0
            dataset = self.dataset()
            start, end = index_range(page, page_size)
            if start > len(dataset):
                return []

            return dataset[start:end]

        except AssertionError as e:
            raise e
