from factory import Factory
from keyboard import Keyboard
from maths.rect import Rect


class Game:
    WIDTH = 320
    HEIGHT = 240
    SCALE = 2
    FPS = 60
    
    def __init__(self):
        self.factory = Factory(self)
        self.keyboard = Keyboard()
        self.entities = []

        self.bg_src_rect = Rect(0, 0, 64, 64)
    
    def start(self):
        self.entities.append(self.factory.create_player(self.WIDTH / 2, self.HEIGHT / 2))
    
    def update(self, delta_time):
        for e in self.entities:
            e.update(delta_time)
    
    def draw(self, sprite_batch):
        # Draw background.
        for x in range(0, self.WIDTH, 64):
            for y in range(0, self.HEIGHT, 64):
                sprite_batch.draw(x, y, self.bg_src_rect)
        
        for e in self.entities:
            e.draw(sprite_batch)
