#!/usr/bin/python3
""" class to define square """


class Square:
    """ class to define square

    attributes:
    size: size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ create an instance of square

        args:
        size: size of square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ getter method fo retreive position of square

        return: position of square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """ setter to position of square

        arg:
        value: value at that position

        raises:
        TypeError:
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for _ in range(self.__position[1]):
                print()
                for _ in range(self.__size):
                    for _ in range(self.__position[0]):
                        print(" ", end="")
                        print("#" * (self.__size))
