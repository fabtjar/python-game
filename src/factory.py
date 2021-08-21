import math
import random

from components.mover import Mover
from components.sprite import Sprite
from entity import Entity
from main import HEIGHT, WIDTH
from maths.rect import Rect


def create_player():
    x = random.randint(0, WIDTH - 32)
    y = random.randint(0, HEIGHT - 32)
    
    e = Entity(x, y)
    
    mover = e.add(Mover())
    angle = random.random() * math.pi * 2
    speed = random.randrange(100, 150)
    mover.speed_x = math.cos(angle) * speed
    mover.speed_y = math.sin(angle) * speed
    
    e.add(Sprite(Rect(64, 0, 32, 32)))
    
    return e
