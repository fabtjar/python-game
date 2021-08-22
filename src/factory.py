from components.collider import Collider, Mask
from components.mover import Mover
from components.player import Player
from components.sprite import Sprite
from components.tiled_sprite import TiledSprite
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
        sprite.draw_order = 10

        e.add(Collider(-16, -32, 32, 32))
        
        return e

    def create_wall(self, x, y):
        e = Entity(self.game, x, y)
        
        e.add(Sprite(Rect(32 * 3, 0, 32, 32)))
        
        collider = e.add(Collider(0, 0, 32, 32))
        collider.masks = (Mask.SOLID,)
    
        return e
    
    def create_background(self):
        e = Entity(self.game, 0, 0)
        
        sprite = e.add(TiledSprite(Rect(0, 0, 64, 64), self.game.WIDTH, self.game.HEIGHT))
        sprite.draw_order = -100
        
        return e
