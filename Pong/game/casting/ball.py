import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point



class Ball(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.set_color(constants.PURPLE)
        self._segments = []
        self._prepare_body()


    def _prepare_body(self):
        x = 0
        y = 0
        position = Point(x, y)
        color = constants.WHITE
#        segment = Actor()
#        segment.set_position(position)
#        segment.set_color(color)
#        self._segments.append(segment)

    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points