import pygame, sys, random
from pygame.locals import *
#khoi dong pygame
pygame.init()
#lay nhieu event khi an giu phim
pygame.key.set_repeat(100, 0)
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
enemy_ammo = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/enemyshot.png")
plane_ammo = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Shot.png")
BACKGROUND1 = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Blue Sky1.png")
BACKGROUND2 = pygame.image.load("C:/Users/210051/Desktop/Pygame Image/Blue Sky1.png")

#Danh sach toa do ammo
list_Ammo = []
list_EnemyAmmo = []
list_EnemyMove = []
#so luong dan toi da cua Enemy tren man hinh
Number_EnemyAmmo = 1
#so luong toi da cua Enemy
Number_Enemy = 1

##Gia tri toc do 
#Toc do Ammo cua Plane nguoi choi
Ammo_speed = 20
#Toc do Enemy
Enemy_Speed = 1
#Toc do Ammo cua Enemy
EnemyAmmo_speed = 40

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

    #ham ve dan cua Plane
    def drawAmmo(self, enemy_pos):
        for count, i in enumerate(list_Ammo):
            #lay toa do Ammo trong list
            xAmmo = i["xAmmo"]
            yAmmo = i["yAmmo"]
            #hien thi ra man hinh
            SURFACE.blit(plane_ammo, (xAmmo, yAmmo))
            #Ammo di chuyen len tren theo toc do Ammo    
            list_Ammo[count]["yAmmo"] = yAmmo - Ammo_speed
            #Khi Ammo gan ra ngoai man hinh thi xoa Ammo
            if yAmmo <= 1 or collision(plane_ammo, (xAmmo, yAmmo), enemy_image, enemy_pos):
                list_Ammo.remove(list_Ammo[count])
                enemy_pos[0] = 1000
            print(enemy_pos)

#class Enemy
class Enemy():
    def draw(self, plane_pos):
        for count, i in enumerate(list_EnemyMove):
            xEnemy = i["xEnemy"]
            yEnemy = i["yEnemy"]
        SURFACE.blit(enemy_image, (xEnemy, yEnemy))
        list_EnemyMove[count]["xEnemy"] = xEnemy + Enemy_Speed
        if xEnemy >= 750:
            list_EnemyMove.remove(list_EnemyMove[count])
        #print(list_Ammo)

    #ham ve dan cua Enemy
    def drawEnemyAmmo(self, plane_pos):
        for count, i in enumerate(list_EnemyAmmo):
            #lay toa do EnemyAmmo trong list
            xEnemyAmmo = i["xEnemyAmmo"]
            yEnemyAmmo = i["yEnemyAmmo"]
            #hien thi ra man hinh
            
            SURFACE.blit(enemy_ammo, (xEnemyAmmo, yEnemyAmmo))
            #EnemyAmmo di chuyen xuong theo toc do Ammo
            list_EnemyAmmo[count]["yEnemyAmmo"] = yEnemyAmmo + EnemyAmmo_speed
            #Khi EnemyAmmo gan ra ngoai man hinh thi xoa EnemyAmmo
            if yEnemyAmmo >= 959 or collision(plane_image, plane_pos, enemy_ammo, (xEnemyAmmo, yEnemyAmmo)) == True:
                list_EnemyAmmo.remove(list_EnemyAmmo[count])
        #print(list_EnemyAmmo)

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

    enemy = Enemy()
    ###thiet lap cac gia tri ban dau
    #vi tri ban dau cua 2 anh nen chuyen dong
    POS1, POS2 = [0, 0], [0, -955]
    #vi tri ban dau cua may bay nguoi choi
    plane_pos = [400, 800]
    #vi tri ban dau cua may bay dich
    enemy_pos = [50, 50]


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
                        "yAmmo": AmmoStart[1] - 70})
                    #print(list_Ammo)

        #Danh sach toa do Ammo cua Enemy
        
        Enemy_AmmoStart = GetCenter(enemy_image,enemy_pos)
        if len(list_EnemyAmmo) < Number_EnemyAmmo:
            list_EnemyAmmo.append({
                "xEnemyAmmo" : Enemy_AmmoStart[0], 
                "yEnemyAmmo" : Enemy_AmmoStart[1]})
        
        #Danh sach toa do Enemy 
        if len(list_EnemyMove) < Number_Enemy:
            list_EnemyMove.append({
                "xEnemy" : enemy_pos[0],
                "yEnemy" : enemy_pos[1]})
        for i in list_EnemyMove:
            enemy_pos = [i["xEnemy"],i["yEnemy"]]
            if enemy_pos[0] >= 750:
                enemy_pos[0] = random.randint(0, 100)
                enemy_pos[1] = random.randint(0, 200)

        #print(enemy_pos)
        #print(list_Ammo)
   
        #ve cac doi tuong
        #ve background
        background.draw(POS1, POS2)
        #ve plane nguoi choi
        plane.draw(plane_pos)
        #ve dan cua plane nguoi choi
        plane.drawAmmo(enemy_pos)
        #ve enemy
        enemy.draw(plane_pos)
        #ve dan cua Enemy
        enemy.drawEnemyAmmo(plane_pos)
        #Cap nhat man hinh
        pygame.display.update()
        #thiet lap FPS
        FPSCLOCK.tick(60)

#khoi chay ham chinh game
if __name__  == "__main__":
    main()
            