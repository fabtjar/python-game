class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    @property
    def w(self):
        return self.width
    
    @property
    def h(self):
        return self.height
