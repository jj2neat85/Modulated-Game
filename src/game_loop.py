import pygame
from os.path import join
import src.collision_detection
import src.draw
import src.config
pygame.init()

# Function to get background tiles and image
def get_background(name):
    # Load background image
    image = pygame.image.load(join("src/assets", "Background", name))
    x, y, width, height = image.get_rect()
    tiles = []

    # Create a grid of background tiles to cover the screen
    for i in range(src.config.WIDTH // width + 1):
        for j in range(src.config.HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    print(tiles)
    return tiles, image


#Configuration before game starts

background, bg_image = get_background( "Blue.png")


def start(game):
    clock = pygame.time.Clock() 
    run = True

    while run:
        clock.tick(src.config.FPS)

        #Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        src.draw.view(game.display.window, background, bg_image, False, False, False)

    pygame.quit()
    quit()