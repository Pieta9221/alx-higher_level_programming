#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    return [x if x != search else replace for x in my_list]
