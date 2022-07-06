#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    
    return (list(map(square, n)) for n in matrix)
 
