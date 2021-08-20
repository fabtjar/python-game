from sdl2 import *
from sdl2.sdlimage import *


WIDTH = 320
HEIGHT = 240
SCALE = 2


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
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)
    SDL_RenderSetScale(renderer, SCALE, SCALE)
    
    surface = IMG_Load(str.encode("assets/tiles.png"))
    texture = SDL_CreateTextureFromSurface(renderer, surface)
    SDL_FreeSurface(surface)
    
    player_x = int(WIDTH / 2) - 16
    player_y = int(HEIGHT / 2) - 16
    
    event = SDL_Event()
    
    running = True
    
    while running:
        SDL_PollEvent(event)
        if event.type == SDL_QUIT:
            running = False
        
        # Draw background.
        for x in range(0, WIDTH, 64):
            for y in range(0, HEIGHT, 64):
                SDL_RenderCopy(renderer, texture, SDL_Rect(0, 0, 64, 64), SDL_Rect(x, y, 64, 64))
        
        # Move player.
        player_x += 2
        player_y += 1
        
        # Wrap around screen.
        if player_x > WIDTH:
            player_x -= WIDTH + 32
        if player_y > HEIGHT:
            player_y -= HEIGHT + 32
        
        # Draw player.
        SDL_RenderCopy(
            renderer, texture, SDL_Rect(64, 0, 32, 32), SDL_Rect(player_x, player_y, 32, 32)
        )
        
        SDL_RenderPresent(renderer)

    SDL_DestroyRenderer(renderer)
    SDL_DestroyTexture(texture)
    SDL_DestroyWindow(window)
    SDL_Quit()


if __name__ == "__main__":
    main()
