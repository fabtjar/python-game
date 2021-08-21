from src.component import Component
from src.main import HEIGHT, WIDTH


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
        
        x = self.entity.x + move_x
        y = self.entity.y + move_y

        # Wrap around screen.
        if x + 32 < 0:
            x += WIDTH + 32
        elif x > WIDTH:
            x -= WIDTH + 32
        if y + 32 < 0:
            y += HEIGHT + 32
        elif y > HEIGHT:
            y -= HEIGHT + 32
        
        self.entity.x = int(x)
        self.entity.y = int(y)
