#!/usr/bin/python3

""" function that multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Return: result multiplication of 2 matrices
    """

    return (np.matmul(m_a, m_b))
