from game.casting.players import Players
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_ball_collision(cast)
            self._handle_segment_collision(cast)
#            self._handle_game_over(cast)

    def _handle_ball_collision(self, cast):
        """Updates the score resets the ball if the ball passes the edge of the screen.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        ball = cast.get_first_actor("ball")
        score_object = cast.get_first_actor("scores")
        position = ball.get_position()
        size_x = ball.get_radius() + ball.get_width()
        if position.get_x() - size_x >= constants.MAX_X:
            score_object.add_points(1, 1)
            ball.set_position(Point(int(constants.MAX_X / 2), int(constants.MAX_Y / 2)))
        elif position.get_x() + size_x <= 0:
            score_object.add_points(1, 2)
            ball.set_position(Point(int(constants.MAX_X / 2), int(constants.MAX_Y / 2)))

    
    def _handle_segment_collision(self, cast):
        """Bounces the ball if it overlaps any paddle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        ball = cast.get_first_actor("ball")
        paddle_point1_1 = player1.get_position().add(Point(player1.get_width(), player1.get_height()))
        paddle_point1_2 = player1.get_position().add(Point(player1.get_width(), player1.get_height()).reverse())
        paddle_point2_1 = player2.get_position().add(Point(player2.get_width(), player2.get_height()))
        paddle_point2_2 = player2.get_position().add(Point(player2.get_width(), player2.get_height()).reverse())
        ball_point = ball.get_position()
        ball_size = Point(ball.get_radius() + ball.get_width(), ball.get_radius() + ball.get_height())
        
        #Check if the ball is colliding with either paddle
        if paddle_point1_1.in_range(paddle_point1_2, ball_point) or paddle_point1_1.in_range(paddle_point1_2, ball_point.add(ball_size)) or paddle_point1_1.in_range(paddle_point1_2, ball_point.add(ball_size.reverse())):
            ball.set_velocity(Point(-1*ball.get_velocity().get_x(), ball.get_velocity().get_y()))
            print("yes")
        elif paddle_point2_1.in_range(paddle_point2_2, ball_point) or paddle_point2_1.in_range(paddle_point2_2, ball_point.add(ball_size)) or paddle_point2_1.in_range(paddle_point2_2, ball_point.add(ball_size.reverse())):
            ball.set_velocity(Point(-1*ball.get_velocity().get_x(), ball.get_velocity().get_y()))
            print("yes")

        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            Player1 = cast.get_first_actor("player1")
            Player2 = cast.get_first_actor("player2")
            segments = Player1.get_segments()
            segments2 = Player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            Player1.set_color(constants.WHITE)
            Player2.set_color(constants.WHITE)
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)