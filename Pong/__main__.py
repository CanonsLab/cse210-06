import constants

from game.casting.cast import Cast
from game.casting.ball import Ball
from game.casting.score import Score
from game.casting.players import Players
from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction

from game.scripting.control_actors_action import ControlActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point



def main():
    
    # create the cast
    cast = Cast()
    P1 = Players()
    P2 = Players()
    P1.set_position(Point(1, 250))
    P2.set_position(Point(880, 250))
    P1.set_color(constants.BLUE)
    P2.set_color(constants.RED)
    cast.add_actor("player1", P1)
    cast.add_actor("player2", P2)

    ball = Ball()
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    ball.set_position(Point(x, y))
    ball.set_velocity(Point(10, 10))
    ball.set_radius(20)
    cast.add_actor("ball", ball)

    scores = Score()
    scores.set_position(Point(397, 0))
    scores.set_font_size(constants.FONT_SIZE)
    scores.set_color(constants.GREEN)
    cast.add_actor("scores", scores)
   
    # start the game
    video_service = VideoService()
    keyboard_service = KeyboardService()

    script = Script()
    script.add_action("output", DrawActorsAction(video_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("input", ControlActorsAction(keyboard_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()