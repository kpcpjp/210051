import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Quest Game")
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
def draw():
    pygame.draw.circle(SURFACE, (255, 0, 0), (scope[0], scope[1]), 20)
def main():
    global scope
    scope = (100, 250)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                scope = event.pos
                print(scope)
        SURFACE.fill(WHITE)
        image = pygame.image.load("C:/Users/khanh/Desktop/New folder/2.png")
        SURFACE.blit(image, (0, 0))
        draw()
        pygame.display.update()
        FPSCLOCK.tick(10)
if __name__ == "__main__":
    main()
