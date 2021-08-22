class Entity:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.components = []
    
    def add(self, component):
        if component not in self.components:
            component.entity = self
            self.components.append(component)
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
    
    def draw(self, sprite_batch):
        for c in self.components:
            c.draw(sprite_batch)
