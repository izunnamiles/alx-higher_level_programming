#!/usr/bin/python3
"""Defines a class square"""
class Square:
    """Square definition"""
    def __init__(self, size=0):
        """
        Initialize the class Square

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
