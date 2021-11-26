import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Quest Game")
SURFACE = pygame.display.set_mode((1280, 720))
FPSCLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)

def main():
    plane = pygame.image.load("C:/Users/210051/Desktop/New folder (3)/13.png")
    background = pygame.image.load("C:/Users/210051/Desktop/New folder (3)/1.jpg")
    pos = (640, 600)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                pos = event.pos
        SURFACE.fill(WHITE)
        SURFACE.blit(background, (0, 0))
        SURFACE.blit(plane, (pos))
        
        pygame.display.update()
        FPSCLOCK.tick(10)
if __name__ == "__main__":
    main()