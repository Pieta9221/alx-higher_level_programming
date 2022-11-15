#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    return {key: 2 * x for key, x in a_dictionary.items()}
