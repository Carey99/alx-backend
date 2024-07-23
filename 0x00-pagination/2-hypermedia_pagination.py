#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List, Dict, Any, Union


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructor"""
        self.__data = None

    def get_data(self, data_file: str) -> List[Dict[str, Any]]:
        """Method that return a list of dictionaries"""
        with open(data_file, 'r') as file:
            data = csv.DictReader(file)
            self.__data = [dict(row) for row in data]
        return self.__data

    def get_page(self, page: int = 1, page_size: int = 10) -> List[Dict[str, Any]]:
        """Method that return the page with the pagination"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start = (page - 1) * page_size
        end = page * page_size
        return self.__data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Method that return a dictionary with the pagination"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__data) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
