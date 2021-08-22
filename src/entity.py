from src.drawable import Drawable


class Entity:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.components = []
    
    def add(self, component):
        if component in self.components:
            raise Exception("Component already in entity.")
        
        component.entity = self
        self.components.append(component)
        if isinstance(component, Drawable):
            self.game.drawables.append(component)
            self.game.update_drawables = True
        return component
    
    def get(self, component_type):
        for c in self.components:
            if isinstance(c, component_type):
                return c
    
    def get_all(self, component_type):
        components = []
        for c in self.components:
            if isinstance(c, component_type):
                components.append(c)
        return components
    
    def update(self, delta_time):
        for c in self.components:
            c.update(delta_time)
