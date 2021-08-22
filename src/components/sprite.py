from src.component import Component
from src.drawable import Drawable


class Sprite(Component, Drawable):
    def __init__(self, src_rect):
        super().__init__()
        self.src_rect = src_rect
        self.offset_x = 0
        self.offset_y = 0
        self.scale_x = 1
        self.scale_y = 1
    
    def draw(self, sprite_batch):
        if self.scale_x == 1 and self.scale_y == 1:
            x = self.entity.x + self.offset_x
            y = self.entity.y + self.offset_y
            return sprite_batch.draw(x, y, self.src_rect)
        
        x = self.entity.x + self.offset_x * self.scale_x
        y = self.entity.y + self.offset_y * self.scale_y
        width = self.src_rect.width * self.scale_x
        height = self.src_rect.height * self.scale_y
        
        sprite_batch.draw_stretched(round(x), round(y), self.src_rect, round(width), round(height))
