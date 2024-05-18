#!/usr/bin/env python3
"""
Implementation of a simple pagination.
"""
import csv
import math
from typing import Dict, List, Tuple


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Handles hypermedia pagination and retrieves info about a page.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        dataset_len = len(self.dataset())
        prev_page = page - 1 if start > 0 else None
        next_page = page + 1 if end and start < dataset_len else None
        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(dataset_len / page_size)
        }
