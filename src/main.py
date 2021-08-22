from sdl2 import *
from sdl2.sdlimage import *

import factory
import keyboard

WIDTH = 320
HEIGHT = 240
SCALE = 2
FPS = 60


def main():
    SDL_Init(SDL_INIT_VIDEO)
    
    window = SDL_CreateWindow(
        str.encode("Python Game"),
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        WIDTH * SCALE,
        HEIGHT * SCALE,
        0
    )
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    SDL_RenderSetScale(renderer, SCALE, SCALE)
    
    surface = IMG_Load(str.encode("../assets/tiles.png"))
    texture = SDL_CreateTextureFromSurface(renderer, surface)
    SDL_FreeSurface(surface)
    
    sprite_batch = SpriteBatch(renderer, texture)
    
    entities = [
        factory.create_player(WIDTH / 2, HEIGHT / 2),
    ]
    
    event = SDL_Event()
    
    running = True
    
    while running:
        old_ticks = SDL_GetTicks()
        
        SDL_PollEvent(event)
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key.repeat == 0:
            keyboard.set_down(event.key.keysym.scancode, True)
        elif event.type == SDL_KEYUP:
            keyboard.set_down(event.key.keysym.scancode, False)
        
        print('main.py', keyboard._keys_down)
        
        # Draw background.
        for x in range(0, WIDTH, 64):
            for y in range(0, HEIGHT, 64):
                SDL_RenderCopy(renderer, texture, SDL_Rect(0, 0, 64, 64), SDL_Rect(x, y, 64, 64))
        
        for e in entities:
            e.update(1 / FPS)
        
        for e in entities:
            e.draw(sprite_batch)
        
        SDL_RenderPresent(renderer)

        new_ticks = SDL_GetTicks()
        if new_ticks - old_ticks < 1000 / FPS:
            SDL_Delay(new_ticks - old_ticks)

    SDL_DestroyRenderer(renderer)
    SDL_DestroyTexture(texture)
    SDL_DestroyWindow(window)
    SDL_Quit()


class SpriteBatch:
    def __init__(self, renderer, texture):
        self.renderer = renderer
        self.texture = texture
    
    def draw(self, x, y, src_rect):
        src_rect = SDL_Rect(
            src_rect.x, src_rect.y, src_rect.width, src_rect.height
        )
        dest_rect = SDL_Rect(x, y, src_rect.w, src_rect.h)
        SDL_RenderCopy(self.renderer, self.texture, src_rect, dest_rect)


if __name__ == "__main__":
    main()
