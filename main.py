import pygame


# hello my name is sophie
# hi my name is can
class Ground:
    def __init__(self, x, y, width, height) -> None:
        grounds.append(self)
        self.rect = pygame.Rect(x, y, width, height)


class JumpMan:
    def __init__(self, x, y) -> None:
        self.rect = pygame.Rect(x, y, 18, 32)
        self.onGround = False
        self.velocityX = 0
        self.velocityY = 0

    def jump(self):
        self.velocityY = -7

    def setVelocityX(self, direction):
        # increses or decreses velocity
        if direction == "d" and self.velocityX < 0:
            self.velocityX += 16 * dt
        elif direction == "a" and self.velocityX > 0:
            self.velocityX -= 16 * dt
        elif direction == "d":
            self.velocityX += 8 * dt
        elif direction == "a":
            self.velocityX -= 8 * dt

        # velocity cap
        if self.velocityX > 4:
            self.velocityX = 4
        elif self.velocityX < -4:
            self.velocityX = -4

    def gravity(self):
        # finds if player is on ground
        self.onGround = False
        for ground in grounds:
            if (
                self.rect.colliderect(ground.rect)
                and player.rect.bottom - 7 <= ground.rect.top
                and self.velocityY > 0
            ):
                player.rect.bottom = ground.rect.top
                self.onGround = True

        # change donwards velocity
        if not self.onGround:
            self.velocityY += 16 * dt
        else:
            self.velocityY = 0
        # speed cap
        if self.velocityY > 8:
            self.velocityY = 8

    def update(self):
        # slows the player down if a or d is not pressed
        if friction:
            if self.velocityX > -0.5 and self.velocityX < -0.5:
                self.velocityX = 0
            elif self.velocityX > 0:
                self.velocityX -= 8 * dt
            elif self.velocityX < 0:
                self.velocityX += 8 * dt

        # moves player
        self.rect.y += self.velocityY
        self.rect.x += self.velocityX


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

player = JumpMan(0, 520)


# this list will hold all of the objects it is named after.
# by going throug these list with a for loop you can run a condition on all instencesn of a class
grounds = []
barrels = []

# place to set up the leval
Ground(0, 550, 252, 32)
Ground(252, 475, 252, 32)
Ground(0, 400, 252, 32)
Ground(252, 325, 252, 32)
Ground(0, 250, 252, 32)
Ground(252, 150, 252, 32)

# Example file showing a basic pygame "game loop"
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.gravity()

    friction = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        friction = False
        player.setVelocityX("a")
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        friction = False
        player.setVelocityX("d")
    if keys[pygame.K_SPACE] and player.onGround:
        player.jump()

    # updates the player (location)
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
