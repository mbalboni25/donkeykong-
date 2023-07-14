import pygame
#hello my name is sophie
#hi my name is can
class Ground:
    def __init__(self, x, y, width, height) -> None:
        grounds.append(self)
        self.reac = pygame.Rect(x, y, width, height)
        


class JumpMan:
    def __init__(self) -> None:
        pass


class Barrel:
    def __init__(self) -> None:
        barrels.append(self)


class Monkey:
    def __init__(self) -> None:
        pass

class Render:
    def __init__(self):
        pass
    def RenderGround(self):
        for ground in grounds:
            pygame.draw.rect(screen, (255, 255, 255), ground.reac, )

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((504, 720))
clock = pygame.time.Clock()
render = Render()


#this list will hold all of the objects it is named after.
#by going throug these list with a for loop you can run a condition on all instencesn of a class 
grounds = []
barrels = []

#place to set up the leval
Ground(0, 536, 252, 32)
Ground(252, 535, 252, 32)


running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER GAME HERE
    render.RenderGround()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()