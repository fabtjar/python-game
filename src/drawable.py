class Drawable:
    def __init__(self):
        self._draw_order = 0
    
    def draw(self, sprite_batch):
        pass
    
    @property
    def draw_order(self):
        return self._draw_order
    
    @draw_order.setter
    def draw_order(self, value):
        self.entity.game.update_drawables = True
        self._draw_order = value
