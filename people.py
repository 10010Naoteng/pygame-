import pygame

class People(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/1.png").convert_alpha()
        self.image2 = pygame.image.load("images/2.png").convert_alpha()
        self.image3 = pygame.image.load("images/3.png").convert_alpha()
        self.image4 = pygame.image.load("images/4.png").convert_alpha()
        self.image5 = pygame.image.load("images/5.png").convert_alpha()
        self.image6 = pygame.image.load("images/6.png").convert_alpha()
        self.image7 = pygame.image.load("images/7.png").convert_alpha()
        self.image8 = pygame.image.load("images/8.png").convert_alpha()
        self.image9 = pygame.image.load("images/9.png").convert_alpha()
        self.image10 = pygame.image.load("images/10.png").convert_alpha()
        self.people = self.image3
        self.mask = pygame.mask.from_surface(self.people)
        self.rect = self.image1.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = 2
        self.i = 0


    def moveLeft(self):
        self.rect.left -= self.speed
        if self.i >= 0 and self.i <= 14:
            self.people = self.image1
        else:
            self.people = self.image2
        self.i += 1
        if self.i == 30:
            self.i = 0

    def moveRight(self):
        self.rect.left += self.speed
        if self.i >= 0 and self.i <= 14:
            self.people = self.image3
        else:
            self.people = self.image4
        self.i += 1
        if self.i == 30:
            self.i = 0

    def moveUp(self):
        self.rect.top -= self.speed
        if self.i >= 0 and self.i <= 9:
            self.people = self.image8
        elif self.i >=10 and self.i <= 19:
            self.people = self.image9
        else:
            self.people = self.image10
        self.i += 1
        if self.i == 30:
            self.i = 0


    def moveDown(self):
        self.rect.top += self.speed
        if self.i >= 0 and self.i <= 9:
            self.people = self.image5
        elif self.i >=10 and self.i <= 19:
            self.people = self.image6
        else:
            self.people = self.image7
        self.i += 1
        if self.i == 30:
           self.i = 0
    
    
    
        
        

