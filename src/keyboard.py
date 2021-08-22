class Keyboard:
    
    RIGHT = 79
    LEFT = 80
    DOWN = 81
    UP = 82
    
    def __init__(self):
        self._keys_down = {}
        self._old_keys_down = {}
        self.name = "init"
    
    def is_down(self, key_code):
        try:
            return self._keys_down[key_code]
        except KeyError:
            return False
    
    def set_down(self, key_code, is_down):
        self._keys_down[key_code] = is_down
    
    def just_pressed(self, key_code):
        try:
            return self._keys_down[key_code] and not self._old_keys_down[key_code]
        except KeyError:
            return False
    
    def just_released(self, key_code):
        try:
            return not self._keys_down[key_code] and self._old_keys_down[key_code]
        except KeyError:
            return False
    
    def update(self):
        _old_keys_down = self._keys_down
