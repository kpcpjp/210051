import pygame, sys
from pygame.locals import *
pygame.init()
#pygame.key.set_repeat(5, 5)
pygame.display.set_caption("空戦")
WHITE = (255, 255, 255)
SCREEN = [800, 960]
SURFACE = pygame.display.set_mode(SCREEN)
FPSCLOCK = pygame.time.Clock()


class Plane():
    def __init__(self):
        self.plane = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/plane.png")
        
    def draw(self, plane_pos):
        self.plane_pos = plane_pos
        SURFACE.blit(self.plane, (plane_pos))
   

class Background():
    def __init__(self):
        self.BACKGROUND1 = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Blue Sky1.png")
        self.BACKGROUND2 = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Blue Sky2.png")
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
        
class Shot():
    def __init__(self):
        self.shot = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Shot.png")
    def move(self, x, y):
        self.x = x
        self.y = y
        shotSurface = pygame.Surface((11, 31), SRCALPHA)
        shotSurface.blit(self.shot, (0 ,0))
        SURFACE.blit(self.shot, (x, y))


def main():
    plane = Plane()
    background = Background()
    plane_pos = [400, 800]
    shot = Shot()
    POS1 = [0, 0]
    POS2 = [0, -955]
    SHOTMOVE = False
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (event.pos[0] in range(0, SCREEN[0]- 15)) and  (event.pos[1] in range(0, SCREEN[1]- 18)):
                    plane_pos = event.pos   
                    #print(plane_pos)
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    SHOTMOVE = True
            elif event.type == KEYUP:
                SHOTMOVE = False
                    

        SURFACE.fill((WHITE))
        background.draw(POS1, POS2)
        plane.draw(plane_pos)
        k = plane_pos[1]
        
        if SHOTMOVE:     
            while k > 0:   
                shot.move(plane_pos[0], k)
                k -= 50
        pygame.display.update()
        FPSCLOCK.tick(60)
if __name__ == "__main__":
    main()