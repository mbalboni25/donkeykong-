import pygame
#hello my name is sophie
#hi my name is can
class Ground:
    def __init__(self, x, y, width, height) -> None:
        grounds.append(self)
        self.rect = pygame.Rect(x, y, width, height)
        


class JumpMan:
    def __init__(self) -> None:
        self.rect = pygame.Rect(0, 0, 18, 32)
        self.velocity = 0
    def setVelocity(self, direction):
        

        #finds if player is on ground
        self.onGround = False
        for ground in grounds:
            if player.rect.bottom == ground.rect.top:
                self.onGround = True
        print(f"player.onGround= {player.onGround}")


        #increses or decreses velocity
        if direction == 'd' and self.velocity < 0:
            self.velocity += 16 * dt
        elif direction == 'a' and self.velocity > 0:
            self.velocity -= 16 * dt
        elif direction == 'd':
            self.velocity += 8 * dt
        elif direction == 'a':
            self.velocity -= 8 * dt
        
        #velocity cap
        if self.velocity > 8:
            self.velocity = 8
        
        
    
    def update(self):
        #slows the player down if a or d is not pressed
        if friction:
            if self.velocity > -0.5 and self.velocity < -0.5:
                self.velocity = 0
            elif self.velocity > 0:
                self.velocity -= 8 * dt
            elif self.velocity < 0:
                self.velocity += 8 * dt
        
        self.rect.x += self.velocity 



class Barrel:
    def __init__(self) -> None:
        barrels.append(self)


class Monkey:
    def __init__(self) -> None:
        pass

class Render:
    def __init__(self):
        pass
    def ground(self):
        for ground in grounds:
            pygame.draw.rect(screen, (255, 255, 255), ground.rect)
    def player(self):
        pygame.draw.rect(screen, (255, 100, 255), player.rect)




# pygame setup
pygame.init()
screen = pygame.display.set_mode((504, 720))
clock = pygame.time.Clock()
dt = 0

render = Render()

player = JumpMan()


#this list will hold all of the objects it is named after.
#by going throug these list with a for loop you can run a condition on all instencesn of a class 
grounds = []
barrels = []

#place to set up the leval
Ground(0, 536, 252, 32)
Ground(252, 535, 252, 32)

# Example file showing a basic pygame "game loop"
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    friction = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        friction = False
        player.setVelocity("a")
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        friction = False
        player.setVelocity("d")

    #updates the player (location)
    player.update()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER GAME HERE
    render.ground()
    render.player()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
