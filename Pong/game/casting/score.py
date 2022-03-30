from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._point_player1 = 0
        self._point_player2 = 0
        self.add_points(0)

    def add_points(self, points, type=1):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
            type (int): Whether to add to player1 or 2 (use player number)
        """
        if type == 1:
            self._point_player1 += points
        elif type == 2:
            self._point_player2 += points
        self.set_text(f"{self._point_player1} : {self._point_player2}")