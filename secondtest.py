import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("空戦")
pygame.key.set_repeat(5, 5)
POS = [800, 960]
SURFACE = pygame.display.set_mode((POS))
FPSCLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
POS1 = [0, 0]
POS2 = [0, -955]
plane_pos = [400, 800]

class Shot():
    pass

def movebackground():
    POS1[1] += 5
    if POS1[1] > 960:
        POS1[1] = 0
    POS2[1] = POS2[1] + 5
    if POS2[1] > 5:
        POS2[1] = -95
class Plane():
    def __init__(self):
        global plane_pos
        if plane_pos[0] < POS[0] and plane_pos[1] < POS[1]:
            if plane_pos[0] > (POS[0]-64) or plane_pos[1] > (POS[1] - 75):
                plane_pos = (plane_pos[0]-64, plane_pos[1] - 75)



def main():
    global plane_pos
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == K_SPACE:
                pass               
            elif event.type == MOUSEMOTION:
                plane_pos = event.pos
        shot_image = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Shot.png")
        BACKGROUND1 = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Blue Sky1.png")
        BACKGROUND2 = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Blue Sky2.png")
        plane = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/13.png")
        SURFACE.fill(WHITE)
        SURFACE.blit(BACKGROUND1, (POS1))
        SURFACE.blit(BACKGROUND2, (POS2))
        Plane()
        SURFACE.blit(plane, (plane_pos))
        movebackground()
        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == "__main__":
    main()