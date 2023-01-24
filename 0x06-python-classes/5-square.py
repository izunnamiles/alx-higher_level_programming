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
        self.size = size

    @property
    def size(self):
        """Get/Set the current size of a square"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Return the area of the square"""
        return pow(self.__size, 2)
    
    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
