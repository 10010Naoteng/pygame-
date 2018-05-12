import pygame
import sys
from pygame.locals import *
import traceback
import people
import wall
import enemy

pygame.init()
pygame.mixer.init()
size = width,height = 999,666
bg = (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("迷宫!")
pygame.mixer.music.load("qq.ogg")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
back = (0,0,0)


def main():
    clock = pygame.time.Clock()
    # i = 0 开始画面
    i = 0
    # 字体
    text_font = pygame.font.Font("AdobeHeitiStd-Regular.otf",35)
    #
    text1 = pygame.image.load('images\kaishi.png').convert_alpha()
    text1_rect = text1.get_rect()
    text1_rect.left,text1_rect.top = width/2-100,height/2-50
    #
    text2 = text_font.render("Game over",True,back)
    text2_rect = text2.get_rect()
    text2_rect.left,text2_rect.top = width/2-50,height/2-50

    text3 = text_font.render("重生",True,back)
    text3_rect = text3.get_rect()
    text3_rect.left,text3_rect.top = width/2-50,height/2+100

    text4 = text_font.render("victory",True,back)
    text4_rect = text4.get_rect()
    text4_rect.left,text4_rect.top = width/2-50,height/2-50
    # 生成小人
    position1 = 0*66,4*66
    position2 = 3*66,9*66
    position3 = 5*66,0*66
    position4 = 7*66,0*66
    position5 = 10*66,0*66
    position6 = 10*66,9*66
    position7 = 14*66,8*66
    position8 = 1*66,0*66
    position9 = 1*66,9*66
    position10 = 3*66,9*66
    position11 = 7*66,9*66
    position12 = 10*66,0*66
    position13 = 12*66,9*66
    position14 = 14*66,4*66
    position15 = 7*66,0*66
    position16 = 7*66,9*66
    position = position1
    me = people.People(position)
    #墙
    wall1_positions = [(0,0),(0,1),(0,2),(0,3),(0,5),(0,6),(0,7),(0,8),(0,9),(1,0),\
                      (1,9),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),\
                      (2,8),(2,9),(3,0),(4,0),(4,1),(4,3),(4,4),(4,5),(4,6),\
                      (4,7),(4,8),(4,9),(5,9),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),\
                      (6,6),(6,7),(6,9),(7,7),(7,9),(8,0),(8,1),(8,2),(8,4),(8,5),(8,6),\
                      (8,7),(8,9),(9,0),(9,7),(9,9),(10,1),(10,2),(10,3),(10,4),\
                      (10,5),(10,7),(11,7),(11,0),(11,9),(12,0),(12,2),(12,3),\
                      (12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(13,0),(13,9),(14,0),\
                      (14,1),(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,9)]
    walls1 = []
    for each in wall1_positions:
        #真实坐标
        position = each[0]*66,each[1]*66
        wa = wall.Wall(position)
        walls1.append(wa)

        
    wall2_positions = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),\
                       (1,7),\
                       (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,7),(2,9),\
                       (3,0),(3,1),(3,2),(3,4),(3,5),(3,7),\
                       (4,0),(4,7),(4,9),\
                       (5,0),(5,2),(5,3),(5,4),(5,5),(5,7),(5,9),\
                       (6,0),(6,5),(6,7),(6,8),(6,9),\
                       (7,0),(7,2),(7,3),(7,5),\
                       (8,0),(8,1),(8,2),(8,3),(8,5),(8,6),(8,7),(8,8),(8,9),\
                       (9,0),(9,1),(9,2),(9,3),(9,7),(9,8),(9,9),\
                       (10,5),(10,8),(10,9),\
                       (11,0),(11,2),(11,3),(11,5),(11,6),(11,9),\
                       (12,0),(12,2),(12,3),(12,5),(12,6),(12,7),\
                       (13,0),(13,5),(13,6),(13,7),(13,8),(13,9),\
                       (14,0),(14,1),(14,2),(14,3),(14,5),(14,6),(14,7),(14,8),(14,9),]
                       
    walls2 = []
    for each in wall2_positions:
        #真实坐标
        position = each[0]*66,each[1]*66
        wa = wall.Wall(position)
        walls2.append(wa)

    wall3_positions = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),\
                       (1,0),(1,9),\
                       (2,0),(2,9),\
                       (3,0),(3,9),\
                       (4,0),(4,9),\
                       (5,0),(5,9),\
                       (6,0),(6,9),\

                       (8,0),(8,9),\
                       (9,0),(9,9),\
                       (10,0),(10,9),\
                       (11,0),(11,9),\
                       (12,0),(12,9),\
                       (13,0),(13,9),\
                       (14,0),(14,1),(14,2),(14,3),(14,4),(14,5),(14,6),(14,7),(14,8),(14,9),]
                       
    walls3 = []
    for each in wall3_positions:
        #真实坐标
        position = each[0]*66,each[1]*66
        wa = wall.Wall(position)
        walls3.append(wa)
    # 生成敌人
    enemys1 = []
    position =  3*66,1*66
    direction = 1
    up =1*66
    down = 8*66
    left = 0
    right = 0
    en = enemy.Enemy((1*66,2*66),1*66,8*66,0,0,1)
    enemys1.append(en)
    en = enemy.Enemy((3*66,4*66),1*66,8*66,0,0,1)
    en.enemy = en.image2
    enemys1.append(en)
    en = enemy.Enemy((5*66,6*66),1*66,8*66,0,0,2)
    en.enemy = en.image2
    enemys1.append(en)
    en = enemy.Enemy((7*66,3*66),1*66,6*66,0,0,2)
    en.enemy = en.image3
    enemys1.append(en)
    en = enemy.Enemy((9*66,3*66),1*66,6*66,0,0,1)
    en.enemy = en.image3
    enemys1.append(en)

    enemys2 = []
    en = enemy.Enemy((4*66,6*66),0,0,1*66,7*66,3)
    en.enemy = en.image2
    enemys2.append(en)
    en = enemy.Enemy((4*66,3*66),1*66,5*66,0,0,1)
    en.enemy = en.image1
    enemys2.append(en)
    en = enemy.Enemy((10*66,4*66),0,0,6*66,13*66,4)
    en.enemy = en.image1
    enemys2.append(en)
    en = enemy.Enemy((10*66,1*66),0,0,10*66,13*66,3)
    en.enemy = en.image1
    enemys2.append(en)
    en = enemy.Enemy((3*66,8*66),0,0,1*66,5*66,3)
    en.enemy = en.image3
    enemys2.append(en)

    enemys3 = []
    en = enemy.Enemy((1*66,1*66),0,0,1*66,13*66,3)
    en.enemy = en.image2
    enemys3.append(en)
    en = enemy.Enemy((2*66,2*66),0,0,1*66,13*66,4)
    en.enemy = en.image3
    en.speed = 2
    enemys3.append(en)
    en = enemy.Enemy((3*66,3*66),0,0,1*66,13*66,3)
    en.enemy = en.image1
    en.speed = 4
    enemys3.append(en)
    en = enemy.Enemy((1*66,4*66),0,0,1*66,13*66,4)
    en.enemy = en.image3
    en.speed = 6
    enemys3.append(en)
    en = enemy.Enemy((6*66,5*66),0,0,1*66,13*66,4)
    en.enemy = en.image3
    en.speed = 8
    enemys3.append(en)
    en = enemy.Enemy((13*66,6*66),0,0,1*66,13*66,3)
    en.enemy = en.image2
    en.speed = 6
    enemys3.append(en)
    en = enemy.Enemy((9*66,7*66),0,0,1*66,13*66,4)
    en.enemy = en.image3
    en.speed = 4
    enemys3.append(en)
    en = enemy.Enemy((7*66,8*66),0,0,1*66,13*66,3)
    en.enemy = en.image1
    en.speed = 2
    enemys3.append(en)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
         #场景1   
        if i == 11:
            #人的移动  限制
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w]:
                me.moveUp()
            if key_pressed[K_s]:
                me.moveDown()
            if key_pressed[K_a]:
                me.moveLeft()
            if key_pressed[K_d]:
                me.moveRight()
            if  pygame.sprite.spritecollide(me,walls1,False,pygame.sprite.collide_mask):
                if key_pressed[K_w]:
                    me.rect.top += me.speed
                if key_pressed[K_s]:
                    me.rect.top -= me.speed
                if key_pressed[K_a]:
                    me.rect.left += me.speed
                if key_pressed[K_d]:
                    me.rect.left -= me.speed
            # 敌人的移动 此处为错误语法  direction会重复赋值
            #en.move_up(up,down,direction)
            for each in enemys1:
                each.move()
                
           
            # 人和鬼的碰撞检测
            if pygame.sprite.spritecollide(me,enemys1,False,pygame.sprite.collide_mask):
                i = 1

            # 人的位置的转换
            if me.rect.left > 3*66 and me.rect.left <4*66 and me.rect.top > 10*66:
                # me.position = position13 对象里已不再引用初始参数position
                me.rect.left,me.rect.top = position13
                i = 12
            if me.rect.left > 5*66 and me.rect.left < 6*66 and me.rect.top < -1*66:
                me.rect.left,me.rect.top = position11
                i = 12
            if me.rect.left > 7*66 and me.rect.left < 8*66 and me.rect.top < -1*66:
                me.rect.left,me.rect.top = position8
                i = 12
            if me.rect.left > 10*66 and me.rect.left < 11*66 and me.rect.top < -1*66:
                me.rect.left,me.rect.top = position12
                i = 12
            if me.rect.left > 10*66 and me.rect.left < 11*66 and me.rect.top > 10*66:
                me.rect.left,me.rect.top = position14
                i = 12
            if me.rect.left > 15*66 and me.rect.top < 9*66 and me.rect.top > 8*66:
                me.rect.left,me.rect.top = position10
                i = 12
            screen.fill(bg)
            for each in walls1:
                screen.blit(each.image2,each.rect)
            screen.blit(me.people,me.rect)
            for each in enemys1:
                screen.blit(each.enemy,each.rect)
            
            #场景2
        if i == 12:
            #人的移动  限制
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w]:
                me.moveUp()
            if key_pressed[K_s]:
                me.moveDown()
            if key_pressed[K_a]:
                me.moveLeft()
            if key_pressed[K_d]:
                me.moveRight()
            if  pygame.sprite.spritecollide(me,walls2,False,pygame.sprite.collide_mask):
                if key_pressed[K_w]:
                    me.rect.top += me.speed
                if key_pressed[K_s]:
                    me.rect.top -= me.speed
                if key_pressed[K_a]:
                    me.rect.left += me.speed
                if key_pressed[K_d]:
                    me.rect.left -= me.speed
            
            for each in enemys2:
                each.move()

            # 人和鬼的碰撞检测
            if pygame.sprite.spritecollide(me,enemys2,False,pygame.sprite.collide_mask):
                i = 1

            #  people 的转换
            if me.rect.left > 1*66 and me.rect.left < 2*66 and me.rect.top < -1*66:
                me.rect.left,me.rect.top = position4
                i = 11
            if me.rect.left > 3*66 and me.rect.left < 4*66 and me.rect.top > 10*66:
                me.rect.left,me.rect.top = position7
                i = 11
            if me.rect.left > 7*66 and me.rect.left < 8*66 and me.rect.top > 10*66:
                me.rect.left,me.rect.top = position3
                i = 11
            if me.rect.left > 10*66 and me.rect.left < 11*66 and me.rect.top < -1*66:
                me.rect.left,me.rect.top = position5
                i = 11
            if me.rect.left > 12*66 and me.rect.left < 13*66 and me.rect.top > 10*66:
                me.rect.left,me.rect.top = position2
                i = 11
            if me.rect.left > 15*66 and me.rect.top < 5*66 and me.rect.top > 4*66:
                me.rect.left,me.rect.top = position6
                i = 11
            if me.rect.left > 1*66 and me.rect.left < 2*66 and me.rect.top > 10*66:
                me.rect.left,me.rect.top = position15
                i = 13
            screen.fill(bg)
            for each in walls2:
                screen.blit(each.image2,each.rect)
            screen.blit(me.people,me.rect)
            for each in enemys2:
                screen.blit(each.enemy,each.rect)
            

        if i == 13:
            #人的移动  限制
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w]:
                me.moveUp()
            if key_pressed[K_s]:
                me.moveDown()
            if key_pressed[K_a]:
                me.moveLeft()
            if key_pressed[K_d]:
                me.moveRight()
            if  pygame.sprite.spritecollide(me,walls3,False,pygame.sprite.collide_mask):
                if key_pressed[K_w]:
                    me.rect.top += me.speed
                if key_pressed[K_s]:
                    me.rect.top -= me.speed
                if key_pressed[K_a]:
                    me.rect.left += me.speed
                if key_pressed[K_d]:
                    me.rect.left -= me.speed
            # 敌人的移动 此处为错误语法  direction会重复赋值
            #en.move_up(up,down,direction)
            for each in enemys3:
                each.move()

            # 人和鬼的碰撞检测
            if pygame.sprite.spritecollide(me,enemys3,False,pygame.sprite.collide_mask):
                i = 1
            
            if me.rect.left > 7*66 and me.rect.left < 8*66 and me.rect.top < -1*66:
                me.rect.left,me.rect.top = position9
                i = 12
            if me.rect.left > 7*66 and me.rect.left < 8*66 and me.rect.top > 9*66:
                i = 2
            screen.fill(bg)
            for each in walls3:
                screen.blit(each.image2,each.rect)
            screen.blit(me.people,me.rect)
            for each in enemys3:
                screen.blit(each.enemy,each.rect)
        if i == 0:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text1_rect.collidepoint(event.pos):
                    i = 11
            screen.fill(bg)
            screen.blit(text1,text1_rect)
        if i == 1:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and text3_rect.collidepoint(event.pos):
                    i = 11
                    me.rect.left,me.rect.top = position1
            screen.fill(bg)
            screen.blit(text2,text2_rect)
            screen.blit(text3,text3_rect)
        if i == 2:
            screen.fill(bg)
            screen.blit(text4,text4_rect)
        pygame.display.flip()
        clock.tick(60)
# 错误显报
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()

