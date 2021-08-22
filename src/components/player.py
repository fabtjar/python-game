from src.component import Component
from src.maths.utils import approach

from .collider import Collider, Mask
from .mover import Mover


class Player(Component):
    MAX_SPEED = 200
    ACCEL = 3000
    DECEL = 1000
    GRAV = 3000
    MAX_GRAV = 900
    JUMP_FORCE = 800
    
    def update(self, delta_time):
        hor = 0
        jump = False
        
        keyboard = self.entity.game.keyboard
        
        if keyboard.is_down(keyboard.LEFT):
            hor -= 1
        if keyboard.is_down(keyboard.RIGHT):
            hor += 1
        if keyboard.just_pressed(keyboard.UP):
            jump = True
        
        mover = self.entity.get(Mover)
        
        # Gravity.
        mover.speed_y = approach(mover.speed_y, self.MAX_GRAV, self.GRAV * delta_time)
        
        # Deceleration.
        mover.speed_x = approach(mover.speed_x, 0, self.DECEL * delta_time)
        
        # Horizontal movement.
        if hor != 0:
            mover.speed_x = approach(mover.speed_x, hor * self.MAX_SPEED, self.ACCEL * delta_time)
        
        # Jumping.
        collider = self.entity.get(Collider)
        on_ground = collider.overlaps_mask(Mask.SOLID, 0, 1)
        if on_ground and jump:
            mover.speed_y = -self.JUMP_FORCE
