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

# create the paddles
class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # write a method on paddle, funtion you can call on
    def draw(self, win):
        # pass where you want to draw (window) it and the color
        pygame.draw.rectangle(win, self.COLOR, (self.x, self.y, self.width, self.height))

# implement drawing with color
def draw(win):
    # update entire window with white
    win.fill(BLACK)
    pygame.display.update()

# main loop to display the window
def main():
    run = True
    # regulate the frame rate of the game
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        draw(WIN)
        # checks for all events being made within the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()
