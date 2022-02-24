import pygame
import random
from pygame import mixer
class Game:
    def __init__(self):
        pygame.init()  # Init pygame
        self.xScreen, self.yScreen = 1000, 960  # Screen create
        self.VBullet = 25  # Tốc độ Bullet
        self.VPlanes = 25  # Tốc độ Planes......./
        self.VEnemy = 6  # Tốc độ Enemy
        self.scores = 0  # Điểm số
        self.numberEnemy = 2  # Số lượng enemy trong một screen
        self.numberBullet = 6  # Số bullet trong một screen
        linkBackGround = 'C:/Users/210051/Desktop/New folder/background.jpg'  # Đường dẫn ảnh background
        self.linkEnemy = 'C:/Users/210051/Desktop/New folder/enemy.png'  # Đường dẫn ảnh Enemy
        self.linkPlanes = 'C:/Users/210051/Desktop/New folder/planes.png'  # Đường dẫn ảnh Planes
        self.sizexPlanes, self.sizeyPlanes = 70, 70
        self.xPlanes, self.yPlanes = self.xScreen / \
            2, self.yScreen-100  # Khởi tao vị trí ban đầu planes
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption("Space Invaders")
        self.background = pygame.image.load(linkBackGround)
        icon = pygame.image.load(self.linkPlanes)
        pygame.display.set_icon(icon)  # Set icon cho screen
        self.gamerunning = True
        self.listBullet = []
        self.listEnemy = []
        self.YGameOver = 0
        self.K_DOWN = self.K_UP = self.K_LEFT = self.K_RIGHT = False
        #self.music("C:/Users/210051/Desktop/New folder/musictheme.wav")
    def music(self, url):  # Âm thanh bắn
        bulletSound = mixer.Sound(url)
        bulletSound.play()
    def show_score(self, x, y, scores, size):  # Hiển thị điểm
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))
    def image_draw(self, url, xLocal, yLocal, xImg, yImg):  # In ra người hình ảnh
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(
            PlanesImg, (xImg, yImg))  # change size image
        self.screen.blit(PlanesImg, (xLocal, yLocal))
    def enemy(self):  # Quản lý Enemy
        for count, i in enumerate(self.listEnemy):
            xEnemy = i["xEnemy"]  # Lấy toạn độ X
            yEnemy = i["yEnemy"]  # Lấy toạn độ Y
            self.YGameOver
            #print("đổi")
            if xEnemy < 0 or xEnemy > self.xScreen-self.sizexPlanes:  # Nếu chạm vào hai bên phải trái
                # thì đổi hướng
                self.listEnemy[count]["direction"] = not self.listEnemy[count]["direction"]
            self.image_draw(self.linkEnemy, xEnemy, yEnemy, self.sizexPlanes,
                            self.sizeyPlanes)  # In enemy ra màn hình
            self.listEnemy[count]["xEnemy"] = xEnemy + \
                (self.VEnemy if self.listEnemy[count]
                 ["direction"] == False else -self.VEnemy)
            self.listEnemy[count]["yEnemy"] = yEnemy + \
                self.VEnemy/2.5  # Toạn độ x xông tốc độ Enemy/3
            # Gán giá trị lớn nhất của Enemy theo y
            self.YGameOver = yEnemy if yEnemy > self.YGameOver else self.YGameOver

            # print(xEnemy,yEnemy,self.xScreen,self.yScreen)
            #print(self.listEnemy[count]["direction"])
    def bullet(self):
        for count, i in enumerate(self.listBullet):
            xBullet = i["xBullet"]  # Lấy trúc tọa độ theo X
            yBullet = i["yBullet"]  # Lấy trúc tọa độ theo Y
            self.image_draw('C:/Users/210051/Desktop/New folder/bullet.png', xBullet,
                            yBullet, 50, 50)  # In ra bullet
            self.listBullet[count]["yBullet"] = yBullet - \
                self.VBullet  # Tiến y vè phía trước
            if yBullet <= 5:  # nếu toạn độ Y phía trên nàm hình thì xóa
                self.listBullet.remove(self.listBullet[count])
        print(self.listBullet)

    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():  # Bắt các sự kiện
                if event.type == pygame.QUIT:  # sự kiện nhấn thoát
                    self.gamerunning = False
                if event.type == pygame.KEYDOWN:  # sự kiện có phím nhấn xuống
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = True
                    if event.key == pygame.K_UP:
                        self.K_UP = True
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = True
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = True
                    if event.key == pygame.K_SPACE:
                        if len(self.listBullet) < self.numberBullet:
                            #bullet music
                            #self.music("C:/Users/210051/Desktop/New folder/laser.wav")
                            self.listBullet.append({  # Add Thêm bullet
                                "xBullet": self.xPlanes+self.sizexPlanes/2 - 25,
                                "yBullet": self.yPlanes-self.sizexPlanes/2,
                            })
                        print(self.listBullet)
                if event.type == pygame.KEYUP:  # sự kiện thả phím
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = False
                    if event.key == pygame.K_UP:
                        self.K_UP = False
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = False
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = False
            if self.K_DOWN:
                self.yPlanes = self.yPlanes+self.VPlanes/2  # TIến lên
            if self.K_UP:
                self.yPlanes = self.yPlanes-self.VPlanes/2  # TIến xuống
            if self.K_LEFT:
                self.xPlanes = self.xPlanes-self.VPlanes  # TIến trái
            if self.K_RIGHT:
                self.xPlanes = self.xPlanes+self.VPlanes  # TIến phải

            # Kiểm tra có vượt quá giới hạn màn hình  và sét về lề màn hình
            self.xPlanes = 0 if self.xPlanes < 0 else self.xPlanes
            self.xPlanes = self.xScreen-self.sizexPlanes if self.xPlanes + \
                self.sizexPlanes > self.xScreen else self.xPlanes
            self.yPlanes = 0 if self.yPlanes < 0 else self.yPlanes
            self.yPlanes = self.yScreen-self.sizeyPlanes if self.yPlanes + \
                self.sizeyPlanes > self.yScreen else self.yPlanes

            # nếu số lượng Enemy ít hơn self.numberEnemy thì tạo thêm
            if len(self.listEnemy) < self.numberEnemy:
                self.listEnemy.append({
                    "xEnemy": random.randint(0, self.xScreen-self.sizexPlanes),
                    "yEnemy": random.randint(-50, self.yScreen/6),
                    "direction": random.choice((True, False))
                })
            listEnemy2 = self.listEnemy
            print(listEnemy2)
            # Kiểm tra có trúng bullet
            for countEnemy, enemyIteam in enumerate(listEnemy2):
                xEnemy = enemyIteam["xEnemy"]
                yEnemy = enemyIteam["yEnemy"]
                xEnemy = enemyIteam["xEnemy"]
                yEnemy = enemyIteam["yEnemy"]
                for countBullet, bulletIteam in enumerate(self.listBullet):
                    xBullet = bulletIteam["xBullet"]
                    yBullet = bulletIteam["yBullet"]
                    # Kiểm tra bullet có nằm giữa Enemy theo trục x không
                    isInX = xEnemy <= xBullet <= xEnemy+self.sizexPlanes
                    # Kiểm tra bullet có nằm giữa Enemy theo trục y không
                    isInY = yEnemy <= yBullet <= yEnemy+self.sizexPlanes/1.2
                    if(isInX and isInY):  # nếu nằm giữa
                        self.listEnemy.remove(
                            self.listEnemy[countEnemy])  # Xóa Enemy
                        self.listBullet.remove(
                            self.listBullet[countBullet])  # Xóa Bullet
                        self.scores = self.scores + 1  # CỘng thêm điểm
                        # print(scores)
                        break
            if self.numberEnemy < 7:
                self.numberEnemy = (self.scores/15) + 2
            if self.YGameOver > self.yScreen-50:  # Nếu Enemy về gần đích
                newGame = False
                #background music
                #self.music("C:/Users/210051/Desktop/New folder/musicbackground.wav")
                while(True):
                    for event in pygame.event.get():   # Nếu nhấn
                        if event.type == pygame.QUIT:  # Thoát
                            self.gamerunning = False
                            newGame = True
                            break
                        if event.type == pygame.KEYDOWN:  # Thoát
                            newGame = True
                            break
                    if(newGame == True):  # Thoát vòng while để vào game mới
                        break
                    self.show_score(100, 100, "Scores:{}".format(
                        self.scores), 40)  # In điểm
                    self.show_score(self.xScreen/2-100, self.yScreen/2-100,
                                    "GAME OVER", 50)  # In Thông báo thua
                    pygame.display.update()
                self.scores = 0      # Trả các biến về giá trị ban đầu
                self.listBullet = []
                self.listEnemy = []
                self.YGameOver = 0
            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)
            # self.show_score(self.xScreen - 200, 20, "duyduysysy@gmail.com", 15)
            #self.image_draw("C:/Users/210051/Desktop/New folder/codelearn-logo.png",
                            #self.xScreen-180, 10, 150, 60)  # Logo code Learn
            self.enemy()
            self.bullet()
            self.image_draw(self.linkPlanes, self.xPlanes,
                            self.yPlanes, self.sizexPlanes, self.sizeyPlanes)
            pygame.display.update()
if __name__ == "__main__":
    game = Game()
    game.run()