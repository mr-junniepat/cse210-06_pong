from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):
    """Controls the racket's movement up and down"""

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        rackets = []
        rackets = cast.get_actors(RACKET_GROUP)
        for i, racket in enumerate(rackets):
            if i == 0:
                if self._keyboard_service.is_key_down(PLAYER_A_KEY_UP): 
                    racket.move_up()
                elif self._keyboard_service.is_key_down(PLAYER_A_KEY_DOWN): 
                    racket.move_down()  
                else: 
                    racket.stop_moving()
            else:
                if self._keyboard_service.is_key_down(PLAYER_B_KEY_UP): 
                    racket.move_up()
                elif self._keyboard_service.is_key_down(PLAYER_B_KEY_DOWN): 
                    racket.move_down()  
                else: 
                    racket.stop_moving()
