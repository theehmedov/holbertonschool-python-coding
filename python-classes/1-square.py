#!/usr/bin/python3
"""Define a square class with a private size attribute"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
