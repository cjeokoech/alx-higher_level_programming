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

        self.size = size

    @property
    def size(self):
        """ getter method to retrieve size of squre

        return: size of square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ setter to set size of square

        args:
        value: size to set for square

        raise:
        TypeError:
        ValueError:
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculate area of square

        return: areas of square
        """

        return self.__size ** 2

    def my_print(self):
        """ to print square to stdout
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
