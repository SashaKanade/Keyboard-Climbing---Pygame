#Sasha Kanade & Brianna Deng
#TEJ207-3
#Mrs. Strelkovska - Period 4
#2025.05.28
#Pygame Final Project
#Version 2

import pygame
import random
import string
import time
random.seed()
pygame.init()
size=(800, 600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Climber - SK BD - Version 1")

#COLORS
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)

#Fonts
font=pygame.font.SysFont('DroidSans',100,True, False)
font2=pygame.font.SysFont('DroidSans', 80, False, False)
font3=pygame.font.SysFont('DroidSans', 25, False, False)
font4=pygame.font.SysFont('DroidSans', 50, False, False)

#Menu
text1=font.render("Keyboard Climbing", True, WHITE)
text2=font2.render("Start", True, BLACK)
text3=font2.render("Instructions", True, BLACK)
text4=font.render("Instructions", True, WHITE)
text5=font3.render("There will be a boulder with a letter above your sprite -- a monkey!", True, WHITE)
text6=font3.render("Your job is to click the correct letter on your keyboard in order to move up and continue playing!", True, WHITE)
text7=font3.render("Remember to click the letter within 10 seconds or you will be sent right back to the beginning!",True, WHITE)
text8=font4.render("Go Back to Menu", True, BLACK)

#IMAGES
backg=pygame.image.load('bg.png')
backg=pygame.transform.scale(backg, (800,600))
boulder=pygame.image.load('boulder.png')
boulder=pygame.transform.scale(boulder, (350,230))
#home=pygame.image.load('homeb.png')
#home=pygame.transform.scale(home, (75,75))

#Sprite
monks=pygame.image.load('Monkey stand.png')
monks=pygame.transform.scale(monks,(200,200))
monkj=pygame.image.load('monkey jump.png')
monkj=pygame.transform.scale(monkj,(200,200))

#Random Letters
lets=[]
for i in range(70):
    l=random.choice(string.ascii_letters)
    lets.append(l)

#Clock
clock = pygame.time.Clock()

menu=True
game=False
Instruc=False

clock=pygame.time.Clock()
counter=0

first=True
#Speeds
speedx1=[]
speedy1=[]

speedx2=[]
speedy2=[]

speedx3=[]
speedy3=[]

speedx=[]
speedy=[]

gravity=0
def jump(type):
    if type==1:
        speedx=speedx1
        speedy=speedy1
    elif type==2








done=False
while not done:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            mx, my=pygame.mouse.get_pos()

            if menu==True:
                if 150<=mx<=650 and 200<=my<=300:
                    menu=False
                    game=True
                elif 150<=mx<=650 and 400<=my<=500:
                    menu=False
                    Instruc=True

            elif Instruc==True:
                if 210<=mx<=610 and 400<=my<=500:
                    Instruc=False
                    menu=True

    mx, my=pygame.mouse.get_pos()
    buttons=pygame.mouse.get_pressed()

    if menu==True:
        screen.blit(backg, (0, 0))
        screen.blit(text1, (80, 100))

        pygame.draw.rect(screen, WHITE, [150, 200, 500, 100])
        pygame.draw.rect(screen, WHITE, [150, 400, 500, 100])
        screen.blit(text2, (340, 215))
        screen.blit(text3, (240, 415))

        if 150<=mx<=650 and 200<=my<=300:
            pygame.draw.rect(screen, BLUE, [150, 200, 500, 100])
            screen.blit(text2, (340, 215))
        if 150<=mx<= 650 and 400<=my<=500:
            pygame.draw.rect(screen, BLUE, [150, 400, 500, 100])
            screen.blit(text3, (240, 415))


    if game==True: #Work in Progress
        screen.blit(backg, (0, 0))

        if first:
            screen.blit(boulder, (440,400))
            screen.blit(monks, (540, 305))

            first = False

        x=random.randint(1,2)
        letter=lets[random.randint(0, 69)]
        letterImg=font2.render(letter, True, WHITE)
        
        if x==1:
            screen.blit(boulder, (440, 75))
            screen.blit(letterImg, (620, 80))

        elif x==2:
            screen.blit(boulder, (60,280))
            screen.blit(letterImg, (220, 290))
        pygame.time.set_timer(10000)
        

        



        
        




        
                
    if Instruc==True:
        screen.blit(backg, (0, 0))
        screen.blit(text4, (200, 100))
        screen.blit(text5, (10, 200))
        screen.blit(text6, (10, 260))
        screen.blit(text7, (10, 320))

        if 210<=mx<=610 and 400<=my<=500:
            pygame.draw.rect(screen, BLUE, [210, 400, 400, 100])
        else:
            pygame.draw.rect(screen, WHITE, [210, 400, 400, 100])

        screen.blit(text8, (260, 430))
    clock.tick(30)
    pygame.display.update()
            
pygame.quit()
