from src import keyboard
from src.component import Component

from .mover import Mover


class Player(Component):
    MAX_SPEED = 100
    ACCEL = 1000
    DECEL = 500
    
    def update(self, delta_time):
        hor, ver = 0, 0

        print('player.py', keyboard._keys_down)

        if keyboard.is_down(keyboard.UP):
            ver -= 1
        if keyboard.is_down(keyboard.DOWN):
            ver += 1
        if keyboard.is_down(keyboard.LEFT):
            hor -= 1
        if keyboard.is_down(keyboard.RIGHT):
            hor += 1
        
        if hor != 0 or ver != 0:
            mover = self.entity.get(Mover)
            mover.speed_x = hor * self.MAX_SPEED
            mover.speed_y = ver * self.MAX_SPEED
