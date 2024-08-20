#!/usr/bin/env python3
''' find correct indices to paginate dataset or return empty list '''
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        '''
        Args: page = 1, page_size = 10
        Return: appropriate page of the dataset
        If input arguments are out of range, return empty list
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        data = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(data):
            return []
        else:
            return data[start_index:end_index]
