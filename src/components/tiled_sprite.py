from src.component import Component
from src.drawable import Drawable
from src.maths.rect import Rect


class TiledSprite(Component, Drawable):
    def __init__(self, src_rect, width, height):
        super().__init__()
        self.src_rect = src_rect
        self.width = width
        self.height = height
    
    def draw(self, sprite_batch):
        for x in range(0, self.width, self.src_rect.width):
            for y in range(0, self.height, self.src_rect.height):
                
                if x + self.src_rect.width <= self.width:
                    width = self.src_rect.width
                else:
                    width = self.width - x
                
                if y + self.src_rect.height <= self.height:
                    height = self.src_rect.height
                else:
                    height = self.height - y
                
                sprite_batch.draw(x, y, Rect(self.src_rect.x, self.src_rect.y, width, height))
