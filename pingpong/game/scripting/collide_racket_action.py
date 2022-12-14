from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketAction(Action):
    """ Handles collisions with the racket, adds a volley for each collision to the score"""
    
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):        
        ball = cast.get_first_actor(BALL_GROUP)
        rackets = []
        rackets = cast.get_actors(RACKET_GROUP)
        for racket in rackets:
            ball_body = ball.get_body()
            racket_body = racket.get_body()

            if self._physics_service.has_collided(ball_body, racket_body):
                stats = cast.get_first_actor(STATS_GROUP)
                stats.add_volley(1)
                ball.bounce_x()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)    