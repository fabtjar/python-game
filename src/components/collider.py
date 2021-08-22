from enum import auto, Enum

from src.component import Component


class Mask(Enum):
    SOLID = auto()


class Collider(Component):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.masks = ()
    
    def overlaps(self, other, offset_x=0, offset_y=0):
        return (
            self.left + offset_x < other.right and
            self.right + offset_x > other.left and
            self.top + offset_y < other.bottom and
            self.bottom + offset_y > other.top
        )
    
    @property
    def left(self):
        return self.x + self.entity.x
    
    @property
    def right(self):
        return self.left + self.width
    
    @property
    def top(self):
        return self.y + self.entity.y
    
    @property
    def bottom(self):
        return self.top + self.height
