import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,position,up,down,left,right,direction):
        pygame.sprite.Sprite.__init__(self)
        # 缩小图片
        self.image1 = pygame.image.load("images/gobo2.gif").convert_alpha()
        self.rect1 = self.image1.get_rect()
        self.image1 = pygame.transform.smoothscale(self.image1,(int(self.rect1.width*0.5),int(self.rect1.height*0.5)))
        self.rect1 = self.image1.get_rect()
        
        self.image2 = pygame.image.load("images/ghoul1-b.png").convert_alpha()
        self.rect2 = self.image2.get_rect()
        self.image2 = pygame.transform.smoothscale(self.image2,(int(self.rect2.width*0.3),int(self.rect2.height*0.3)))
        self.rect2 = self.image2.get_rect()
        
        self.image3 = pygame.image.load("images/ghost2-a.png").convert_alpha()
        self.rect3 = self.image3.get_rect()
        self.image3 = pygame.transform.smoothscale(self.image3,(int(self.rect3.width*0.3),int(self.rect3.height*0.3)))
        self.rect3 = self.image3.get_rect()
        
        self.t_image1 = pygame.transform.flip(self.image1,True,False)
        self.t_image2 = pygame.transform.flip(self.image2,True,False)
        self.t_image3 = pygame.transform.flip(self.image3,True,False)
        self.enemy = self.image1
        self.rect = self.image1.get_rect()
        self.speed = 1
        #必须为此格式
        self.rect.left,self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image1)
        self.direction = direction
        self.up = up
        self.down = down
        self.left = left
        self.right = right

# 下列的方法单独的 up 不能由上面的 提供 要变换一下
    def move(self):
        # 1代表向上 2代表向下 3代表向左 4代表向右
        if self.direction == 1:
            self.rect.top -= self.speed
        if self.direction == 2:
            self.rect.top += self.speed
        if self.direction == 1 or self.direction == 2:
            if self.rect.top < self.up:
                self.direction = 2
            if self.rect.top > self.down:
                self.direction = 1

        if self.direction == 3:
            self.rect.left -= self.speed
        if self.direction == 4:
            self.rect.left += self.speed
        if self.direction == 3 or self.direction == 4:
            if self.rect.left < self.left:
                self.direction = 4
            if self.rect.left > self.right:
                self.direction = 3

