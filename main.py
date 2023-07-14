import pygame
#hello my name is sophie
#hi my name is can
class Ground:
    def __init__(self) -> None:
        pass


class JumpMan:
    def __init__(self) -> None:
        pass


class Barrel:
    def __init__(self) -> None:
        pass


class Monkey:
    def __init__(self) -> None:
        pass


# a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((504, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window or CMD+Q on mac
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()