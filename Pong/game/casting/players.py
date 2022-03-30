from turtle import width
import constants
from game.casting.actor import Actor
from game.shared.point import Point
import pyray




class Players(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    
    def _prepare_body(self):
        x = 0
        y = 0
        self._width = 20
        self._height = 80
        self._color = constants.ORANGE
        position = Point(x, y)
        color = constants.ORANGE
#        segment = Actor()
#        segment.set_position(position)
#        segment.set_color(color)
#        segment.set_width(width)
#        segment.set_height(height)
#        self._segments.append(segment)
        # for i in range(constants.SNAKE_LENGTH):
        #     position = Point(x - i * constants.CELL_SIZE, y)
        #     velocity = Point(1 * constants.CELL_SIZE, 0)
        #     text = "8" if i == 0 else "#"
        #     color = constants.YELLOW if i == 0 else constants.GREEN
            
        #     segment = Actor()
        #     segment.set_position(position)
        #     segment.set_velocity(velocity)
        #     segment.set_text(text)
        #     segment.set_color(color)
        #     self._segments.append(segment)
    def set_position(self, position):
        y = super().get_position()
        change = position.subtract(y)
        for i in self._segments:
            x = i.get_position()
            i.set_position(x.add(change))
        return super().set_position(position)
    
    def move_next(self):
        y = (self._position.get_y() + self._velocity.get_y())
        if y + self._radius + self._height >= constants.MAX_Y:
            self._position = Point(self._position.get_x(), constants.MAX_Y - self._height - self._radius)
        if y <= 0:
            self._position = Point(self._position.get_x(), 0)
        return super().move_next()