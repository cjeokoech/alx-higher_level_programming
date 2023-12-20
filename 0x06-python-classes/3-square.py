#!/usr/bin/python3
""" class to define square """


class Square:
    """ class to define square

    attributes:
    size: size of square
    """

    def __init__(self, size=0):
        """ create an instance of square

        args:
        size: size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """ calculate area of square

        return: areas of square
        """

        return self.__size ** 2
