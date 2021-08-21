from src.component import Component


class Sprite(Component):
    def __init__(self, src_rect):
        self.src_rect = src_rect
        self.offset_x = 0
        self.offset_y = 0
    
    def draw(self, sprite_batch):
        x = self.entity.x + self.offset_x
        y = self.entity.y + self.offset_y
        sprite_batch.draw(x, y, self.src_rect)
