from src.component import Component


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
