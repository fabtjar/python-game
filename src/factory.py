from components.mover import Mover
from components.player import Player
from components.sprite import Sprite
from entity import Entity
from maths.rect import Rect


class Factory:
    def __init__(self, game):
        self.game = game
    
    def create_player(self, x, y):
        e = Entity(self.game, x, y)
        
        e.add(Player())
        e.add(Mover())
        
        sprite = e.add(Sprite(Rect(64, 0, 32, 32)))
        sprite.offset_x = -16
        sprite.offset_y = -32
        
        return e
