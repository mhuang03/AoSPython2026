# ============================================================
#  PONG
#  a simple pong game against the computer
#
#  Read the pygame documentation: https://www.pygame.org/docs/
# ============================================================

import pygame
import random
import math

# --- setup ---------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 640, 480          # size of the window (in pixels)
FPS = 60                          # frames per second (how fast the game runs)
SPEED = 6

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 60)   # big font for the score


# --- game objects --------------------------------------------

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 90)   # (x, y, width, height)
        self.speed = 6

    def move(self, dy):
        self.rect.y += dy
        self.rect.clamp_ip(screen.get_rect())   # keep it on the screen

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.reset()

    def reset(self):
        # track the exact position with decimals (self.x, self.y) and copy
        # it into the rect each frame. That lets the ball travel at angles
        # while keeping its speed exactly constant.
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        # launch toward a random side at a shallow random angle
        self.dy = random.uniform(-0.4, 0.4) * SPEED
        self.dx = random.choice([-1, 1]) * math.sqrt(SPEED ** 2 - self.dy ** 2)
        self.rect.center = (round(self.x), round(self.y))

    def bounce(self, paddle, direction):
        #   -1.0 = top edge, 0 = middle, +1.0 = bottom edge
        offset = (self.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
        offset = max(-1, min(1, offset))            # keep it in the -1..1 range

        # the closer to the edge you hit, the steeper the angle. The SPEED
        # stays the same, we just split it differently between dx and dy.
        # direction is +1 to send the ball right, -1 to send it left.
        self.dy = offset * SPEED * 0.8
        self.dx = direction * math.sqrt(SPEED ** 2 - self.dy ** 2)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (round(self.x), round(self.y))

        # bounce off the top and bottom walls
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y = self.rect.centery
            self.dy = -self.dy
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.y = self.rect.centery
            self.dy = -self.dy

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)


# left paddle = you, right paddle = the computer
player = Paddle(30, HEIGHT // 2 - 45)
computer = Paddle(WIDTH - 45, HEIGHT // 2 - 45)
computer.speed = 4          # a little slower than you, so it is beatable

ball = Ball()

player_score = 0
computer_score = 0


# --- game loop -----------------------------------------------
running = True
while running:

    # (a) handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # (b) update

    # your paddle: move with the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(-player.speed)
    if keys[pygame.K_DOWN]:
        player.move(player.speed)

    # computer paddle: it follows the ball, but only reacts once the
    # ball is on its half of the court, which gives you a fair chance.
    # (the +10 / -10 is a small "dead zone" that stops it from jittering)
    if ball.rect.centerx > WIDTH // 2:
        if ball.rect.centery > computer.rect.centery + 10:
            computer.move(computer.speed)
        elif ball.rect.centery < computer.rect.centery - 10:
            computer.move(-computer.speed)

    # move the ball
    ball.update()

    # bounce the ball off a paddle
    # we also check the ball's direction so it can't get stuck inside a paddle.
    if ball.rect.colliderect(player.rect) and ball.dx < 0:
        ball.bounce(player, 1)        # send it back to the right
    if ball.rect.colliderect(computer.rect) and ball.dx > 0:
        ball.bounce(computer, -1)     # send it back to the left

    # someone scores when the ball leaves the left or right edge
    if ball.rect.left <= 0:
        computer_score += 1
        ball.reset()
    if ball.rect.right >= WIDTH:
        player_score += 1
        ball.reset()

    # (c) draw
    screen.fill(BLACK)

    # dashed line down the middle
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, y, 4, 15))

    player.draw(screen)
    computer.draw(screen)
    ball.draw(screen)

    # scores: yours on the left, the computer's on the right
    player_text = font.render(str(player_score), True, WHITE)
    computer_text = font.render(str(computer_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 2 - 60, 20))
    screen.blit(computer_text, (WIDTH // 2 + 30, 20))

    pygame.display.flip()
    clock.tick(FPS)


# --- cleanup -------------------------------------------------
pygame.quit()