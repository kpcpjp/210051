import pygame, sys
from pygame.locals import *
pygame.init()
pygame.key.set_repeat(5, 5)
pygame.display.set_caption("空戦")
SURFACE = pygame.display.set_mode((800, 960))
FPSCLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)

class Plane():
    def __init__(self):
        self.plane = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/13.png")
        
    def draw(self, plane_pos):
        self.plane_pos = plane_pos
        SURFACE.blit(self.plane, (plane_pos))
   

class Background():
    def __init__(self):
        self.BACKGROUND1 = pygame.image.load("C:/Users/210051\Desktop/Pygame Image/Blue Sky1.png")
    def draw(self, POS1):
        self.POS1 = POS1
        SURFACE.blit(self.BACKGROUND1, POS1)
    def bg_move(self, POS1, POS2):
        POS1 = [0, 0]
        POS2 = [0, -955]
        if  POS1[1] >= 960:
            POS1[1] = 0
        else:
            POS1[1] += 5
        if POS2[1] >= 5:
            POS2[1] = -955
        else:
            POS2[1] += 5

class Shot:
    pass




def main():
    plane = Plane()
    background = Background()
    plane_pos = [400, 800]
    POS1 = [0, 0]
    POS2 = [0, -955]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                plane_pos = event.pos     
        SURFACE.fill((WHITE))
        background.draw(POS1)
        plane.draw(plane_pos)
        pygame.display.update()
        FPSCLOCK.tick(10)
if __name__ == "__main__":
    main()