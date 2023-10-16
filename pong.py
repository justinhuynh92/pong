import pygame
pygame.init()

# set width and height of window
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# define frames per second
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# create the paddles
class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # write a method on paddle, funtion you can call on
    def draw(self, win):
        # pass where you want to draw (window) it and the color
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    # call method on the paddle if up is true
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

# create the ball
class Ball:
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        # pass the win, color and radius
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    # move the ball
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

# implement drawing with color
def draw(win, paddles, ball):
    # update entire window with white
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    # draw line in the middle of the screen
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    ball.draw(win)
    pygame.display.update()

# move paddles up and down
def handle_paddle_movement(keys, left_paddle, right_paddle):
    # prevent paddles from moving off screen
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

# main loop to display the window
def main():
    run = True
    # regulate the frame rate of the game
    clock = pygame.time.Clock()

    # pass x, y, width, and height
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # initialize the ball
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)
        # checks for all events being made within the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()
