import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/q1.png").convert_alpha()
        self.image2 = pygame.image.load("images/q2.png").convert_alpha()
        self.image3 = pygame.image.load("images/q3.png").convert_alpha()
        self.rect = self.image1.get_rect()
        #必须为此格式
        self.rect.left,self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image1)

