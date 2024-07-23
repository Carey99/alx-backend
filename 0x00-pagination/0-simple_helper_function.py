#!/usr/bin/env python3
"""
    takes 2 args page & page_size
    return tuple of size two containing start and end  idx
    corresponding to the range of idx  to return in a lisst
    for those particular pagintion params
"""


def index_range(page: int, page_size: int) -> tuple:
    """ return tuple of size two containing start and end  idx """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
