import pygame
import random
import string
import time
import os
random.seed()
pygame.init()
size=(800, 600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Climber - SK BD - Version 2")

#COLORS
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)

#Fonts
font=pygame.font.SysFont('DroidSans',100,True, False)
font2=pygame.font.SysFont('DroidSans', 80, False, False)
font3=pygame.font.SysFont('DroidSans', 25, False, False)
font4=pygame.font.SysFont('DroidSans', 50, False, False)

#Images
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

first=True
#Speeds
speedx1=0
speedy1=41

speedx2=-41
speedy2=-13.7

speedx3=41
speedy3=13.7

speedx=0
speedy=0

gravity=-1
def jump(type):
    if type==1:
        speedx=speedx1
        speedy=speedy1
        gravity=-2

    elif type==2:
        speedx=speedx2
        speedy=speedy2
        gravity=-2
        d
    elif type==3:
        speedx=speedx3
        speedy=speedy3
        gravity=-2
        

b1pos=[]
b2pos=[]
#code
clock=pygame.time.Clock()
done=False
while not done:
    clock.tick(60)
    
    pos=pygame.mouse.get_pos()
    x1=pos[0]
    y2=pos[1]
        
    textImg=font3.render(f"x = {x1}, y = {y2}", True, WHITE)
    screen.blit(backg, (0, 0))
    screen.blit(textImg, [x1+15, y2-5])
    screen.blit(boulder, (440,400))
    screen.blit(monks, (540, 305))
    screen.blit(boulder, (60, 280))
    screen.blit(boulder, (440, 75))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

        if first:
            screen.blit(boulder, (440,400))
            screen.blit(monks, (540, 305))

            first = False

        x=random.randint(1,2)
        letter=lets[random.randint(0, 69)]
        letterImg=font2.render(letter, True, WHITE)


    clock.tick(30)
    pygame.display.update()
            
pygame.quit()
