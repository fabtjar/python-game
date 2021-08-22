from src.component import Component
from src.maths.utils import approach, normalise

from .mover import Mover


class Player(Component):
    MAX_SPEED = 200
    ACCEL = 2000
    DECEL = 500
    GRAV = 3000
    MAX_GRAV = 800
    
    def update(self, delta_time):
        hor = 0
        
        keyboard = self.entity.game.keyboard
        
        if keyboard.is_down(keyboard.LEFT):
            hor -= 1
        if keyboard.is_down(keyboard.RIGHT):
            hor += 1
        
        mover = self.entity.get(Mover)
        
        # Gravity.
        mover.speed_y = approach(mover.speed_y, self.MAX_GRAV, self.GRAV * delta_time)
        
        # Deceleration.
        mover.speed_x = approach(mover.speed_x, 0, self.DECEL * delta_time)
        
        if hor != 0:
            mover.speed_x = approach(mover.speed_x, hor * self.MAX_SPEED, self.ACCEL * delta_time)
