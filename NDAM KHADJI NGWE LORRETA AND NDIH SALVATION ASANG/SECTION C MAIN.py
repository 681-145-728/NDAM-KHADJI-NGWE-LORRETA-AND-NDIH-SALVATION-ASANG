# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:59:23 2024

@author: laureta
"""
#Simple rectangle
class Rectangle:
    """Empty class Rectangle that defines a rectangle."""
    pass

#Real definition of a rectangle
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
# Area and Perimeter
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    #String representation
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        
        return "\n".join(["#" * self.width for _ in range(self.height)])
    
    #Eval is magic
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

#Detect instance deletion
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

#How many instances
  class Rectangle:
    """Class Rectangle that defines a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Remaining methods from previous tasks...

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)

#Change representation

class Rectangle:
    """Class Rectangle that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Remaining methods from previous tasks...

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width for _ in range(self.height)])

#Compare rectangles
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Remaining methods from previous tasks...

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

#A square is a rectangle
class Rectangle:
    """Class Rectangle that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"


