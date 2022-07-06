#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is not None:
        return [list(map(lambda x: x.replace('search', 'replace'), my_list))]
    return None
