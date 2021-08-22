from src.component import Component
from src.maths.utils import sign

from .collider import Collider, Mask


class Mover(Component):
    def __init__(self, speed_x=0, speed_y=0):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.remainder_x = 0
        self.remainder_y = 0
    
    def update(self, delta_time):
        
        self.remainder_x += self.speed_x * delta_time
        self.remainder_y += self.speed_y * delta_time
        move_x = round(self.remainder_x)
        move_y = round(self.remainder_y)
        self.remainder_x -= move_x
        self.remainder_y -= move_y
        
        self.move_x(move_x)
        self.move_y(move_y)
        
        x = self.entity.x
        y = self.entity.y

        # Wrap around screen.
        width = self.entity.game.WIDTH
        height = self.entity.game.HEIGHT
        if x + 16 < 0:
            x += width + 32
        elif x - 16 > width:
            x -= width + 32
        if y < 0:
            y += height + 32
        elif y - 32 > height:
            y -= height + 32
        
        self.entity.x = int(x)
        self.entity.y = int(y)
    
    def move_x(self, move_x):
        if move_x == 0:
            return
        
        collider = self.entity.get(Collider)
        sign_x = sign(move_x)
        
        while move_x != 0:
            if collider.overlaps_mask(Mask.SOLID, sign_x, 0):
                self.stop_x()
                break
            self.entity.x += sign_x
            move_x -= sign_x

    def move_y(self, move_y):
        if move_y == 0:
            return
    
        collider = self.entity.get(Collider)
        sign_y = sign(move_y)
    
        while move_y != 0:
            if collider.overlaps_mask(Mask.SOLID, 0, sign_y):
                self.stop_y()
                break
            self.entity.y += sign_y
            move_y -= sign_y
    
    def stop_x(self):
        self.speed_x = self.remainder_x = 0
    
    def stop_y(self):
        self.speed_y = self.remainder_y = 0
