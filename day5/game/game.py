# ============================================================
#  PYGAME TEMPLATE
#  Fill in the sections marked TODO to turn it into your own game!
#
#  Read the pygame documentation: https://www.pygame.org/docs/
# ============================================================

import pygame
import random          # useful for random positions, speeds, and choices


# --- setup ------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 640, 480          # size of the window (in pixels)
FPS = 60                          # frames per second (how fast the game runs)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")   # text in the window's title bar
clock = pygame.time.Clock()

# a few colors to use, each is (red, green, blue), values from 0 to 255.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 60, 60)
BLUE  = (60, 120, 220)
GREEN = (60, 200, 100)

# a font for drawing text on the screen (like the score)
font = pygame.font.SysFont(None, 36)



# --- game objects ---------------------------------------
# Here is an example class for a player you control with the
# arrow keys. Try changing the color, the size, or the speed!

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)   # (x, y, width, height)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep the player from leaving the screen
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)


# Create the objects your game needs
player = Player(WIDTH // 2, HEIGHT // 2)
score = 0

# TODO: create any other objects your game needs here
#       (for example: a falling item, a target, or a list of enemies)


# --- game loop -----------------------------------------------
# everything inside this loop runs ~60 times per second
running = True
while running:

    # (a) handle events: quitting, mouse clicks, single key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TODO: respond to a mouse click here, if your game needs it
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = event.pos

    # (b) update: move things, check collisions, change the score
    keys = pygame.key.get_pressed()
    player.update(keys)

    # TODO: move your other objects and check for collisions
    #       Example:
    #       if player.rect.colliderect(item.rect):
    #           score += 1

    # (c) draw: this happens fresh every frame
    screen.fill(BLACK)                  # clear the screen first
    player.draw(screen)                 # draw the player

    # TODO: draw your other objects here

    # Draw the score in the top-left corner
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()               # show the newly drawn frame
    clock.tick(FPS)                     # pause so the game runs at the right speed


# --- cleanup ----------------------------------------------
pygame.quit()