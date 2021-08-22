from sdl2 import *
from sdl2.sdlimage import *

from game import Game


class App:
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        
        self.game = Game()
        
        self.window = SDL_CreateWindow(
            str.encode("Python Game"),
            SDL_WINDOWPOS_UNDEFINED,
            SDL_WINDOWPOS_UNDEFINED,
            Game.WIDTH * Game.SCALE,
            Game.HEIGHT * Game.SCALE,
            0
        )
        self.renderer = SDL_CreateRenderer(
            self.window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
        )
        SDL_RenderSetScale(self.renderer, Game.SCALE, Game.SCALE)
        
        self.surface = IMG_Load(str.encode("../assets/tiles.png"))
        self.texture = SDL_CreateTextureFromSurface(self.renderer, self.surface)
        SDL_FreeSurface(self.surface)
        
        self.sprite_batch = SpriteBatch(self.renderer, self.texture)
        self.event = SDL_Event()
    
    def start(self):
        self.game.start()

        running = True
        while running:
            old_ticks = SDL_GetTicks()
            
            self.game.keyboard.update()
            
            SDL_PollEvent(self.event)
            if self.event.type == SDL_QUIT:
                running = False
            elif self.event.type == SDL_KEYDOWN and self.event.key.repeat == 0:
                self.game.keyboard.set_down(self.event.key.keysym.scancode, True)
            elif self.event.type == SDL_KEYUP:
                self.game.keyboard.set_down(self.event.key.keysym.scancode, False)
            
            self.game.update(1 / Game.FPS)
            self.game.draw(self.sprite_batch)
            
            SDL_RenderPresent(self.renderer)
    
            new_ticks = SDL_GetTicks()
            if new_ticks - old_ticks < 1000 / Game.FPS:
                SDL_Delay(new_ticks - old_ticks)
    
    def destroy(self):
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyTexture(self.texture)
        SDL_DestroyWindow(self.window)
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
    
    def draw_stretched(self, x, y, src_rect, width, height):
        src_rect = SDL_Rect(
            src_rect.x, src_rect.y, src_rect.width, src_rect.height
        )
        dest_rect = SDL_Rect(x, y, width, height)
        SDL_RenderCopy(self.renderer, self.texture, src_rect, dest_rect)


if __name__ == "__main__":
    app = App()
    app.start()
    app.destroy()
