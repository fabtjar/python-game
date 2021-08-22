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
        self.drawables = []
        self.update_drawables = False

        self.bg_src_rect = Rect(0, 0, 64, 64)
    
    def start(self):
        self.entities.append(self.factory.create_player(self.WIDTH / 2, self.HEIGHT / 2))
        self.entities.append(self.factory.create_wall(32 * 2, 32 * 2))
        self.entities.append(self.factory.create_wall(32 * 3, 32 * 5))
        self.entities.append(self.factory.create_wall(32 * 7, 32 * 3))
        self.entities.append(self.factory.create_wall(32 * 7, 32 * 4))
    
    def update(self, delta_time):
        for e in self.entities:
            e.update(delta_time)
    
    def draw(self, sprite_batch):
        if self.update_drawables:
            self.drawables.sort(key=lambda d: d.draw_order)
            self.update_drawables = False
        
        # Draw background.
        for x in range(0, self.WIDTH, 64):
            for y in range(0, self.HEIGHT, 64):
                sprite_batch.draw(x, y, self.bg_src_rect)
        
        for d in self.drawables:
            d.draw(sprite_batch)
    
    def get(self, component_type):
        for e in self.entities:
            c = e.get(component_type)
            if c is not None:
                return c
    
    def get_all(self, component_type):
        components = []
        for e in self.entities:
            for c in e.components:
                if isinstance(c, component_type):
                    components.append(c)
        return components
