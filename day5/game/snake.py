# ============================================================
#  SNAKE
#  eat all the apples
#
#  Read the pygame documentation: https://www.pygame.org/docs/
# ============================================================

import pygame
import random

# --- setup ---------------------------------------------------
pygame.init()

WIDTH, HEIGHT = 640, 480          # size of the window (in pixels)
FPS = 60                          # frames per second
CELL = 20                         # size of one grid square (in pixels)
COLS = WIDTH // CELL              # number of columns in the grid (32)
ROWS = HEIGHT // CELL             # number of rows in the grid (24)
MOVE_DELAY = 8                    # move the snake every 8 frames (smaller = faster)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 60, 60)
GREEN = (60, 200, 100)
DARK  = (40, 140, 70)

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 48)


# --- game objects --------------------------------------------

class Snake:
    def __init__(self):
        # the snake is a list of (column, row) squares; the head is first.
        # start as a length-3 snake in the middle, moving to the right.
        start_col = COLS // 2
        start_row = ROWS // 2
        self.body = [
            (start_col, start_row),
            (start_col - 1, start_row),
            (start_col - 2, start_row),
        ]
        self.direction = (1, 0)         # (dx, dy): (1, 0) means moving right
        self.next_direction = (1, 0)
        self.grow = False

    def change_direction(self, new_direction):
        # ignore a turn that would make the snake reverse straight into itself.
        dx, dy = self.direction
        if new_direction != (-dx, -dy):
            self.next_direction = new_direction

    def move(self):
        self.direction = self.next_direction
        head_col, head_row = self.body[0]
        dx, dy = self.direction
        new_head = (head_col + dx, head_row + dy)
        self.body.insert(0, new_head)       # add the new head at the front

        if self.grow:
            self.grow = False               # keep the tail this step (grew by 1)
        else:
            self.body.pop()                 # otherwise drop the tail (same length)

    def hits_wall(self):
        col, row = self.body[0]
        return col < 0 or col >= COLS or row < 0 or row >= ROWS

    def hits_self(self):
        # did the head land on any other part of the body?
        return self.body[0] in self.body[1:]

    def draw(self, surface):
        for i, (col, row) in enumerate(self.body):
            color = GREEN if i == 0 else DARK     # the head is a bit brighter
            rect = (col * CELL, row * CELL, CELL, CELL)
            pygame.draw.rect(surface, color, rect)


def random_food(snake_body):
    # pick a random empty square for the food
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake_body:
            return pos


# --- create the starting game state --------------------------
snake = Snake()
food = random_food(snake.body)
score = 0
game_over = False
move_timer = 0


# --- game loop -----------------------------------------------
running = True
while running:

    # (a) handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_SPACE:
                    # restart the game
                    snake = Snake()
                    food = random_food(snake.body)
                    score = 0
                    game_over = False
                    move_timer = 0
            else:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

    # (b) update
    if not game_over:
        # the snake only steps forward every MOVE_DELAY frames, so the game
        # stays responsive at 60 FPS without the snake zooming across instantly
        move_timer += 1
        if move_timer >= MOVE_DELAY:
            move_timer = 0
            snake.move()

            # eat the food?
            if snake.body[0] == food:
                snake.grow = True
                score += 1
                food = random_food(snake.body)

            # crashed into a wall or itself?
            if snake.hits_wall() or snake.hits_self():
                game_over = True

    # (c) draw
    screen.fill(BLACK)

    # food
    food_rect = (food[0] * CELL, food[1] * CELL, CELL, CELL)
    pygame.draw.rect(screen, RED, food_rect)

    # snake
    snake.draw(screen)

    # score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # game over message
    if game_over:
        over_text = big_font.render("Game Over", True, WHITE)
        info_text = font.render("Press SPACE to play again", True, WHITE)
        screen.blit(over_text, over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        screen.blit(info_text, info_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))

    pygame.display.flip()
    clock.tick(FPS)


# --- cleanup -------------------------------------------------
pygame.quit()