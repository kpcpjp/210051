import pygame, sys
from pygame.locals import *
pygame.init()
pygame.key.set_repeat(5, 5)
pygame.display.set_caption("空戦")
WHITE = (255, 255, 255)
SCREEN = [800, 960]
SURFACE = pygame.display.set_mode(SCREEN)
FPSCLOCK = pygame.time.Clock()


class Plane():
    def __init__(self):
        self.plane = pygame.image.load("C:/Users/khanh/Python 3.9/Pygame/First pygame/Image/plane.png")
        
    def draw(self, plane_pos):
        self.plane_pos = plane_pos
        SURFACE.blit(self.plane, (plane_pos))
   

class Background():
    def __init__(self):
        self.BACKGROUND1 = pygame.image.load("C:/Users/khanh/Python 3.9/Pygame/First pygame/Image/Blue Sky1.png")
        self.BACKGROUND2 = pygame.image.load("C:/Users/khanh/Python 3.9/Pygame/First pygame/Image/Blue Sky2.png")
    def draw(self, POS1, POS2):
        self.POS1 = POS1
        self.POS2 = POS2
        while POS1[1] < 961:
            SURFACE.blit(self.BACKGROUND1, POS1)
            if  POS1[1] == 960:
                POS1[1] = 0
            else:
                POS1[1] += 5
            #print(POS1)
            break
        while POS2[1] < 6:
            SURFACE.blit(self.BACKGROUND2, POS2)
            if  POS2[1] == 5:
                POS2[1] = -955
            else:
                POS2[1] += 5
            #print(POS2)
            break
        
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
                if (event.pos[0] in range(0, SCREEN[0]- 15)) and  (event.pos[1] in range(0, SCREEN[1]- 18)):
                    plane_pos = event.pos   
                    print(plane_pos)
        SURFACE.fill((WHITE))
        background.draw(POS1, POS2)
        plane.draw(plane_pos)
        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == "__main__":
    main()