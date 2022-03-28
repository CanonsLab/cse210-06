class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    
    def subtract(self, other):
        """Gets a new point that starts at this, reduced by the given one.

        Args:
            other (Point): The Point to remove.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x - other.get_x()
        y = self._y - other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def in_range(self, other, comp):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The opposing point.
            comp (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        x1 = self._x
        y1 = self._y
        x2 = other.get_x()
        y2 = other.get_y()
        if x1 < x2:
            x_low = x1
            x_high = x2
        else:
            x_low = x2
            x_high = x1
        if y1 < y2:
            y_low = y1
            y_high = y2
        else:
            y_low = y2
            y_high = y1
        x_comp = comp.get_x()
        y_comp = comp.get_y()
        return x_low <= x_comp and y_low <= y_comp and x_high >= x_comp and y_high >= y_comp

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def reverse(self):
        """Reverses the point by inverting both x and y values.

        Returns:
            Point: A new point that is reversed.
        """
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)
