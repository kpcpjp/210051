import pygame, sys
from pygame.locals import *
#khoi dong pygame
pygame.init()
#lay nhieu event khi an giu phim
pygame.key.set_repeat(50, 0)
#set kich thuoc va tao man hinh chinh game
DISPLAY = [800, 960]
SURFACE = pygame.display.set_mode(DISPLAY)
#set tieu de man hinh
pygame.display.set_caption("Air Battle")
#set khung FPS
FPSCLOCK = pygame.time.Clock()
#load cac hinh anh, am thanh trong game
plane_image = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/plane.png")
enemy_image = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/enemy1.png")
plane_ammo = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Shot.png")
BACKGROUND1 = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Blue Sky1.png")
BACKGROUND2 = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Blue Sky1.png")

#danh sach toa do ammo
list_Ammo = []
#toc do Ammo
Ammo_speed = 30

#class anh nen game
class Background():
    #ham ve chuyen dong anh nen game theo kich thuoc man hinh chinh
    def draw(self, POS1, POS2):
        self.POS1 = POS1
        self.POS2 = POS2
        while POS1[1] < 961:
            SURFACE.blit(BACKGROUND1, POS1)
            if  POS1[1] == 960:
                POS1[1] = 0
            else:
                POS1[1] += 5
            break
        while POS2[1] < 6:
            SURFACE.blit(BACKGROUND2, POS2)
            if  POS2[1] == 5:
                POS2[1] = -955
            else:
                POS2[1] += 5  
            break

#class may bay nguoi choi
class Plane():
    #ham ve may bay nguoi choi
    def draw(self, plane_pos):
        self.plane_pos = plane_pos
        SURFACE.blit(plane_image, (plane_pos))

#class Ammo
class Ammo():
    def draw(self, enemy_pos):
        for count, i in enumerate(list_Ammo):
            #lay toa do dan trong list
            xAmmo = i["xAmmo"]
            yAmmo = i["yAmmo"]
            #hien thi ra man hinh
            SURFACE.blit(plane_ammo, (xAmmo, yAmmo))
            #Ammo di chuyen len tren theo toc do Ammo
            list_Ammo[count]["yAmmo"] = yAmmo - Ammo_speed
            #Khi Ammo gan ra ngoai man hinh thi xoa dan
            if yAmmo <= 5 or collision(plane_ammo, (xAmmo, yAmmo), enemy_image, enemy_pos) == True:
                list_Ammo.remove(list_Ammo[count])
        #print(list_Ammo)

#class Enemy
class Enemy():
    def draw(self, enemy_pos):
        SURFACE.blit(enemy_image,enemy_pos)

#Hàm lấy tọa độ trung tâm
def GetCenter(image, pos):
    x = pos[0] + image.get_width() // 2
    y = pos[1] + image.get_height() // 2
    center = (x, y)
    return center

#Ham xu li va cham cua 2 doi tuong dua vao vi tri cua no (pos1, pos2)
def collision(surface1, pos1, surface2, pos2):
    mask1 = pygame.mask.from_surface(surface1)
    mask2 = pygame.mask.from_surface(surface2)
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    #print(x, y)
    if mask1.overlap(mask2, (x, y)) != None:
        return True
    return False

#Ham chinh cua game
def main():
    #thiet lap cac doi tuong
    background = Background()
    plane = Plane()
    ammo = Ammo()
    enemy = Enemy()
    ###thiet lap cac gia tri ban dau
    #vi tri ban dau cua 2 anh nen chuyen dong
    POS1, POS2 = [0, 0], [0, -955]
    #vi tri ban dau cua may bay nguoi choi
    plane_pos = [400, 800]
    #vi tri ban dau cua may bay dich
    enemy_pos = [400, 200]


    #vong lap chinh game
    while True:
        #lay va thao tac voi event trong game
        for event in pygame.event.get():
            #khi nhan nut thoat thi thoat game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #may bay di chuyen theo vi tri chuot
            elif event.type == MOUSEMOTION:
                #vi tri may bay khong ra ngoai man hinh
                if (event.pos[0] in range(0, DISPLAY[0]- 15)) and  (event.pos[1] in range(0, DISPLAY[1]- 18)):
                    plane_pos = event.pos 
            #ban Ammo
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    #list_Ammo
                    AmmoStart = GetCenter(plane_image, plane_pos)
                    list_Ammo.append({
                        "xAmmo": AmmoStart[0],
                        "yAmmo": AmmoStart[1]})
                    #print(list_Ammo)


        #ve cac doi tuong
        background.draw(POS1, POS2)
        plane.draw(plane_pos)
        ammo.draw(enemy_pos)
        enemy.draw(enemy_pos)
        #Cap nhat man hinh
        pygame.display.update()
        #thiet lap FPS
        FPSCLOCK.tick(60)

#khoi chay ham chinh game
if __name__  == "__main__":
    main()
            