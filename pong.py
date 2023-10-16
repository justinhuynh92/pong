import pygame
pygame.init()

# set width and height of window
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# define frames per second
FPS = 60

# main loop to display the window
def main():
    run = True
    # regulate the frame rate of the game
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        # checks for all events being made within the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()
