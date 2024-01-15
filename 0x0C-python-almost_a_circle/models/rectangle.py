#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherit from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectagle instance

        Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x(int, optional): X-coordinate of the top-left corner (default is 0).
        y (int, optional): Y-coordinate of the top-left corner (default is 0).
        id (int, optional): Unique identifier for the
        rectangle (default is None).
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """width getter"""

            return self.__width

        @width.setter
        def width(self, value):
            """Width setter"""

            if not isinstance(value, int) or isinstance(value, bool):
                raise TyprError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

            @property
            def height(self):
                """Height getter"""

                return self.__height

            @height.setter
            def height(self, value):
                """height setter"""
                if not isinstance(value, int):
                    raise TypeError("height must be integer")
                if value <= 0:
                    raise ValueError("height must be > 0")
                self.__height = value

                @property
                def x(self):
                    """X coordinates of rectangle"""

                    return self.__x

                @x.setter
                def x(self, value):
                    """X setter"""

                    if not isinstance(value, int):
                        raise TypeError("x must be an integer")
                    if value < 0:
                        raise ValueError("x must be > 0")
                    self.__x = value

                    @property
                    def y(self):
                        """Y getters"""

                        return self.__y

                    @y.setter
                    def y(self, value):
                        """Y setters"""

                        if not isinstance(value, int):
                            raise TypeError("y must be an integer")
                        if value < 0:
                            raise ValueError("y must be > 0")
                        self.__y = value

                        def area(self):
                            """Return the area of rectangle"""
                            area = self.width * self.height
                            return area

                        def display(self):
                            """print rectangle with instance #"""
                            for i in range(self.y):
                                print()
                                for i in range(self.height):
                                    print(" " * self.x + "#" * self.width)

                                    def __str__(self):
                                        """
                                        Return the print() and str() representation of the Rectangle.
                                        """
                                        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

                                        def update(self, *args, **kwargs):
                                            """
                                            Assign arguments to attributes based on their positions.
                                            """
                                            if args:
                                                for count, arg in enumerate(args):
                                                    if count == 0:
                                                        self.id = arg
                                                        elif count == 1:
                                                            self.width = arg
                                                            elif count == 2:
                                                                self.height = arg
                                                                elif count == 3:
                                                                    self.x = arg
                                                                    elif count == 4:
                                                                        self.y = arg
                                                                    else:
                                                                        break
                                                                    elif len(kwargs) > 0:
                                                                        for key, value in kwargs.items():
                                                                            if key == "id":
                                                                                self.id = value
                                                                                elif key == "width":
                                                                                    self.width = value
                                                                                    elif key == "height":
                                                                                        self.height = value
                                                                                        elif key == "x":
                                                                                            self.x = value
                                                                                            elif key == "y":
                                                                                                self.y = value

                                                                                                def to_dictionary(self):
                                                                                                    """
                                                                                                    Represents a dictionary representation of rectangle
                                                                                                    """
                                                                                                    rec_dict = {
                                                                                                            "id": self.id,
                                                                                                            "width": self.width,
                                                                                                            "height": self.height,
                                                                                                            "x": self.x
                                                                                                            "y": self.y
                                                                                                            }
                                                                                                    return rec_dict

                                                                                                if __name__ == "__main__":
                                                                                                    pass
