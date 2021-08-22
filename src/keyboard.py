_keys_down = {}
_old_keys_down = {}


def is_down(key_code):
    try:
        return _keys_down[key_code]
    except KeyError:
        return False


def set_down(key_code, is_key_down):
    _keys_down[key_code] = is_key_down


def just_pressed(key_code):
    try:
        return _keys_down[key_code] and not _old_keys_down[key_code]
    except KeyError:
        return False


def just_released(key_code):
    try:
        return not _keys_down[key_code] and _old_keys_down[key_code]
    except KeyError:
        return False


def update():
    global _old_keys_down
    _old_keys_down = _keys_down


RIGHT = 79
LEFT = 80
DOWN = 81
UP = 82
