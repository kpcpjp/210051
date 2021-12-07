import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("空戦")
SURFACE = pygame.display.set_mode((800, 960))
FPSCLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
POS1 = [0, 0]
POS2 = [0, -955]
plane_pos = [400, 800]

class Drawable:
    def __init__(self):
        shot_image = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Shot.png")
        BACKGROUND1 = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Blue Sky1.png")
        BACKGROUND2 = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Blue Sky2.png")
        plane = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/13.png")
        SURFACE.blit(BACKGROUND1, (POS1))
        SURFACE.blit(BACKGROUND2, (POS2))
        SURFACE.blit(plane, (plane_pos))
class movement:
    def __init__(self):
        if POS1[1] >= 960:
            POS1[1] = 0
        else:
            POS1[1] += 5
        if POS2[1] >= 5:
            POS2[1] = -955
        else:
            POS2[1] += 5

def main():
    global plane_pos
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                plane_pos = event.pos   
                print(plane_pos)
        SURFACE.fill((WHITE))
        Drawable()
        movement()
        pygame.display.update()
        FPSCLOCK.tick(10)
if __name__ == "__main__":
    main()