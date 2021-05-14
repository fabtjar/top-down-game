import sdl2
from sdl2 import *
from sdl2 import sdlimage

WIDTH = 320
HEIGHT = 240
SCALE = 3

FPS = 60

frame_delay = 1000 // FPS
frame_start = 0
frame_time = 0

SDL_Init(SDL_INIT_VIDEO)

window = SDL_CreateWindow(
    str.encode("top down game"),
    SDL_WINDOWPOS_UNDEFINED,
    SDL_WINDOWPOS_UNDEFINED,
    WIDTH * SCALE,
    HEIGHT * SCALE,
    0
)

renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)
SDL_RenderSetScale(renderer, SCALE, SCALE)

surface = sdlimage.IMG_Load(str.encode("tiles.png"))
texture = SDL_CreateTextureFromSurface(renderer, surface)
SDL_FreeSurface(surface)

SDL_SetRenderDrawColor(renderer, 100, 149, 237, 255)

running = True

x = 100
y = 50
vel_x = 2
vel_y = 1

event = SDL_Event()
while running:
    SDL_PollEvent(event)
    if event.type == SDL_QUIT:
        running = False
        
    frame_start = SDL_GetTicks()
    
    if x + vel_x < 0 or x + vel_x + 16 > WIDTH:
        vel_x *= -1
    x += vel_x
    
    if y + vel_y < 0 or y + vel_y + 16 > HEIGHT:
        vel_y *= -1
    y += vel_y
    
    SDL_RenderClear(renderer)
    SDL_RenderCopy(renderer, texture, SDL_Rect(0, 0, 16, 16), SDL_Rect(x, y, 16, 16))
    SDL_RenderPresent(renderer)
    
    frame_time = SDL_GetTicks() - frame_start
    
    if frame_delay > frame_time:
        SDL_Delay(frame_delay)

SDL_DestroyWindow(window)
SDL_DestroyRenderer(renderer)
SDL_DestroyTexture(str.encode("tiles.png"))
SDL_Quit()
