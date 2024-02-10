# -*- coding: utf-8 -*-
"""

@author: laureta
"""

# 0-rectangle.py
class Rectangle:
    """Empty class"""
    pass

# 1-rectangle.py
class Rectangle:

    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
        
        # 2-rectangle.py
class Rectangle:
   
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


# 3-rectangle.py
class Rectangle:
    """Rectangle class with area, perimeter, and string representation."""
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

# 4-rectangle.py
class Rectangle:
   
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
    
    def __repr__(self):
        """Representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

# 5-rectangle.py
class Rectangle:
   
    
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
    
    def __repr__(self):
        """Representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Delete an instance of Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

# 6-rectangle.py
class Rectangle:
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)
    
    def __repr__(self):
        """Representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Delete an instance of Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

# 7-rectangle.py
class Rectangle:
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)
    
    def __repr__(self):
        """Representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Delete an instance of Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

# 8-rectangle.py
class Rectangle:
   
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)
    
    def __repr__(self):
        """Representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Delete an instance of Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        """Create a square where width == height == size."""
        return cls(size, size)

# 9-rectangle.py
class Rectangle:
    
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set width with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieve height."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set height with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)
    
    def __repr__(self):
        """Representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Delete an instance of Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        """Create a square where width == height == size."""
        return cls(size, size)


        
