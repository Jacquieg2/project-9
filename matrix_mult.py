# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 03/04/2025
# Description: multiplying funcations

def dot_prod(list1, list2):
    """
    Computes the dot product of two lists of numbers.
    """
    return sum(a * b for a, b in zip(list1, list2))

def matrix_mult(matrix_A, matrix_B):
    """
    Multiplies two matrices (lists of lists) together.
    Returns the resulting matrix or None if multiplication is not possible.
    """
    if len(matrix_A[0]) != len(matrix_B):  
        return None  # Matrices cannot be multiplied due to mismatched dimensions

    # Transpose matrix_B to get its columns as lists
    matrix_B_T = list(zip(*matrix_B))

    # Compute the resulting matrix using dot products
    result = [[dot_prod(row, col) for col in matrix_B_T] for row in matrix_A]
    
    return result
