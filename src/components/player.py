from src.component import Component
from src.maths.utils import approach

from .collider import Collider, Mask
from .mover import Mover
from .sprite import Sprite


class Player(Component):
    MAX_SPEED = 200
    ACCEL = 3000
    DECEL = 1000
    GRAV = 3000
    MAX_GRAV = 900
    JUMP_FORCE = 800
    SCALE_SPEED = 3
    
    def __init__(self):
        self.was_on_ground = False
    
    def update(self, delta_time):
        collider = self.entity.get(Collider)
        mover = self.entity.get(Mover)
        sprite = self.entity.get(Sprite)

        # Bounce scale back to 1.
        sprite.scale_x = approach(sprite.scale_x, 1, self.SCALE_SPEED * delta_time)
        sprite.scale_y = approach(sprite.scale_y, 1, self.SCALE_SPEED * delta_time)
        
        hor = 0
        jump = False
        
        keyboard = self.entity.game.keyboard
        
        if keyboard.is_down(keyboard.LEFT):
            hor -= 1
        if keyboard.is_down(keyboard.RIGHT):
            hor += 1
        if keyboard.just_pressed(keyboard.UP):
            jump = True
        
        # Gravity.
        mover.speed_y = approach(mover.speed_y, self.MAX_GRAV, self.GRAV * delta_time)
        
        # Deceleration.
        mover.speed_x = approach(mover.speed_x, 0, self.DECEL * delta_time)
        
        # Horizontal movement.
        if hor != 0:
            mover.speed_x = approach(mover.speed_x, hor * self.MAX_SPEED, self.ACCEL * delta_time)
        
        on_ground = collider.overlaps_mask(Mask.SOLID, 0, 1)
        
        # Squash if landing.
        if on_ground and not self.was_on_ground:
            sprite.scale_x = 1.5
            sprite.scale_y = 0.5
        self.was_on_ground = on_ground

        # Jumping.
        if on_ground and jump:
            mover.speed_y = -self.JUMP_FORCE
            sprite.scale_x = 0.5
            sprite.scale_y = 1.8
