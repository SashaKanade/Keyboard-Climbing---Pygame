#Sasha Kanade & Brianna Deng
#TEJ207-3
#Mrs. Strelkovska - Period 4
#2025.06.06
#Pygame Final Project
#Final Version
#SUBMITTED CODE BUGS FIXED

import pygame
import random
import string
pygame.init()
size=(800, 600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Climbing - SK BD - Final Version")

'''SK and BD'''

#COLORS
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)
DARKRED=(139, 0, 0)

#FONTS
customfont=pygame.font.SysFont('DroidSans', 40)
customfont1=pygame.font.SysFont('DroidSans', 20)
customfont2=pygame.font.SysFont('DroidSans', 80)
font2=pygame.font.SysFont('DroidSans', 80, False, False)
font3=pygame.font.SysFont('DroidSans', 30, False, False)
font4=pygame.font.SysFont('DroidSans', 50, False, False)

#MENU
title=customfont.render("Keyboard Climbing", True, WHITE)
start=customfont.render("Start", True, BLACK)
instructions1=customfont.render("Instructions", True, BLACK)
instructions2=customfont.render("Instructions", True, WHITE)
text1=font3.render("1. There will be a boulder with a letter above or beside your sprite--a monkey!", True, WHITE)
text2=font3.render("2. Your job is to press the correct lowercase letter on your keyboard", True, WHITE)
text3=font3.render("in order to move your sprite up to the boulder and continue playing!", True, WHITE)
text4=font3.render("3. Remember to press the letter shown within 10 seconds or you will be", True, WHITE)
text5=font3.render("sent right back to the beginning!", True, WHITE)
text6=font3.render("4. The goal is to get a score of 50! Have fun and may the fastest time win!", True, WHITE)
goback=customfont1.render("Go Back to Menu", True, BLACK)
youwin=customfont.render("YOU WIN!", True, WHITE)
utime=customfont.render("Your time:" ,True, WHITE)
bt1=customfont1.render("Try again for a better time",True, WHITE)
bt2=customfont1.render("or challenge your friends!",True, WHITE)
gameover1=customfont2.render("GAME", True, DARKRED)
gameover2=customfont2.render("OVER", True, DARKRED)

#IMAGES
backg=pygame.image.load('bg.png')
backg=pygame.transform.scale(backg, (800, 600))
boulder=pygame.image.load('boulder.png')
boulder=pygame.transform.scale(boulder, (350, 230))
homeb=pygame.image.load('homeb.png')
homeb=pygame.transform.scale(homeb, (75, 75))
gameover=pygame.image.load('gameover.png')
gameover=pygame.transform.scale(gameover, (800, 600))
finaleimg=pygame.image.load('finale.png')
finaleimg=pygame.transform.scale(finaleimg, (800, 600))

#SPRITE
monks=pygame.image.load('Monkey stand.png')
monks=pygame.transform.scale(monks,(200, 200))
monkj=pygame.image.load('monkey jump.png')
monkj=pygame.transform.scale(monkj,(200, 200))
rmonkj=pygame.image.load('monkey jump.png')
rmonkj=pygame.transform.scale(rmonkj,(200, 200))
rmonks=pygame.image.load('Monkey stand.png')
rmonks=pygame.transform.scale(rmonks,(200, 200))

#Random Letters
lets=[]
lets.append("a")
for i in range(100):
    l=random.choice(string.ascii_letters)
    l=l.lower()
    lets.append(l)
letter=lets[0]

'''
#Speeds
speedx1=0
speedy1=41

speedx2=-41
speedy2=-13.7

speedx3=41
speedy3=13.7

speedx=0
speedy=0
'''

#Jump
jump1=False
jump2=False
xspeed=540
yspeed=305
jcount=0

#State
menu=True
game=False
instruc=False
correct=False
fail=False
finale=False

#Stopwatch
s=0
sec=0
mins=0
stopwatchImg=customfont1.render("0:00", True, WHITE)

#Variables
counter=0
x=540
y=305
x2=160
y2=185
order=0
bposition=1
score=0

#Shift
scount=0
shift=False

clock=pygame.time.Clock()

done=False
while not done:

    clock.tick(60) 
    correct=False
    '''
    #Mouse Position
    pos=pygame.mouse.get_pos()
    x1=pos[0]
    y1=pos[1]
    textImg=font3.render(f"x = {x1}, y = {y1}", True, WHITE)
    screen.blit(backg, (0, 0))
    screen.blit(textImg, [x1+15, y1-5])
    '''
    screen.blit(backg, (0, 0))
    
    #Letter
    if counter==0 or counter==600:
        order+=1
        if order==100:
            order=0
        letter=lets[order]
    letterImg=customfont.render(letter, True, WHITE)
    
    #Counter for Time
    counter+=1
    counter=counter%1200
    
    #Boulder Position
    if counter<600 or score==0:
        bposition=1
    elif counter>=600:
        bposition=2
           
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            mx,my=pygame.mouse.get_pos()

            if menu==True:
                if 150<=mx<=650 and 200<=my<=300:
                    menu=False
                    game=True
                    score=0
                    mins=0
                    sec=0
                    s=0
                    shift=False
                    
                elif 150<=mx<=650 and 400<=my<=500:
                    menu=False
                    instruc=True

            elif instruc==True:
                if 210<=mx<=610 and 400<=my<=500:
                    instruc=False
                    menu=True

            elif game==True:
                if 5<=mx<=80 and 5<=my<=80:
                    game=False
                    menu=True
                    
            elif fail==True:
                if 100<=mx<=700 and 450<=my<=550:
                    fail=False
                    menu=True
                    
        if event.type==pygame.KEYDOWN:
            if event.key==ord(letter):
                print(ord(letter), event.key)
                correct=True
            else:
                game=False
                fail=True
                
    mx,my=pygame.mouse.get_pos()
    buttons=pygame.mouse.get_pressed()

    if menu==True:
        screen.blit(backg, (0, 0))
        screen.blit(title, (75, 100))

        pygame.draw.rect(screen, WHITE, [150, 200, 500, 100])
        pygame.draw.rect(screen, WHITE, [150, 400, 500, 100])
        screen.blit(start, (300, 225))
        screen.blit(instructions1, (165, 425))

        if 150<=mx<=650 and 200<=my<=300:
            pygame.draw.rect(screen, BLUE, [150, 200, 500, 100])
            screen.blit(start, (300, 225))
        if 150<=mx<=650 and 400<=my<=500:
            pygame.draw.rect(screen, BLUE, [150, 400, 500, 100])
            screen.blit(instructions1, (165, 425))

    if game==True:
        #Home Button
        screen.blit(homeb, (5, 5))
        
        #Boulders and Monkey
        if bposition==1:  #Brianna's Code - J1
            if shift==True:
                if scount<=280:
                    scount+=5
                    screen.blit(boulder, (60, 320+scount))
                    
                    screen.blit(boulder, (440, 115+scount))
                    screen.blit(monks, (x, 20+scount))
                    
                    screen.blit(boulder, (60, 0+scount))
                    screen.blit(letterImg, (230, 0+scount))
                elif scount>280:
                    shift=False
                    
            if shift==False:
                    screen.blit(boulder, (440, 400))
                    screen.blit(monks, (x, y))
                    
                    screen.blit(boulder, (60, 280))
                    screen.blit(letterImg, (230, 280))

            if correct==True:
                if score==0:
                    xspeed=540
                    yspeed=305
                    counter=0
                score+=1
                if score==50:
                    finale=True
                    game=False
                    
                print("correct, jump")
                jump1=True

            if jump1==True:
                screen.blit(backg, (0, 0))
                if jcount<20:
                    jcount+=1
                    xspeed-=20
                    yspeed-=20-1.1*jcount
                    if jcount==20:
                        jump1=False
                screen.blit(boulder, (440, 400))
                screen.blit(boulder, (60, 280))
                screen.blit(monkj, (xspeed, yspeed))
                screen.blit(homeb, (5, 5))

            if jump1==False and jcount==20:
                screen.blit(monkj, (210, 210))
                pygame.time.delay(20)
                jcount=0
                xspeed=160
                yspeed=185
                counter=600
                scount=0
                shift=True
                
            if correct==False and counter==599:
                print("fail")
                game=False
                fail=True
                
        elif bposition==2:  #Sasha's Code - J2
            if shift==True:
                if scount<=40:
                    scount+=2
        
                    screen.blit(boulder, (60, 280+scount))
                    screen.blit(rmonks, (x2, y2+scount))
                    
                    screen.blit(boulder, (440, 75+scount))
                    screen.blit(letterImg, (610, 75+scount))
                elif scount>40:
                    shift=False
                    
            if shift==False:
                    screen.blit(boulder, (60, 320))
                    screen.blit(rmonks, (x2, 225))
                    
                    screen.blit(boulder, (440, 115))
                    screen.blit(letterImg, (610, 115))
                    
            if correct==True:
                score+=1
                if score==50:
                    finale=True
                    game=False
                    
                print("correct, jump")
                jump2=True
                    
            if jump2==True:
                screen.blit(backg, (0, 0))
                if jcount<20:
                    jcount+=1
                    xspeed+=18
                    yspeed-=20-0.9*jcount
                    if jcount==20:
                        jump2=False
                screen.blit(boulder, (60, 320))
                screen.blit(boulder, (440, 115))
                screen.blit(rmonkj, (xspeed, yspeed))
                screen.blit(homeb, (5, 5))

            if jump2==False and jcount==20:
                screen.blit(rmonkj, (540, 20))
                pygame.time.delay(20)
                jcount=0
                xspeed=540
                yspeed=305
                counter=0
                scount=0
                shift=True
                    
            elif correct==False and counter==1199:
                print("fail")
                game=False
                fail=True
                
        #Stopwatch
        s+=1
        s%=60
        if s==0:
            sec+=1
            if sec==60:
                mins+=1
                sec=0
            if sec<10:
                stopwatchImg=customfont1.render(f"{mins}:0{sec}", True, WHITE)
            else:
                stopwatchImg=customfont1.render(f"{mins}:{sec}", True, WHITE)
        screen.blit(stopwatchImg, (380, 5))

        #Score
        scoree=customfont1.render(f"Score: {score}", True, WHITE)
        screen.blit(scoree, (600, 5))

    if fail==True:
        screen.blit(gameover, (0, 0))
        screen.blit(gameover1, (230, 200))
        screen.blit(gameover2, (230, 275))
        pygame.draw.rect(screen, WHITE, [100, 450, 600, 100])
        screen.blit(goback, (250, 485))
        if 100<=mx<=700 and 450<=my<=550:
            pygame.draw.rect(screen, DARKRED, [100, 450, 600, 100])
            screen.blit(goback, (250, 485))
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                fail=False
                menu=True
                game=False

    if finale==True:
        screen.blit(finaleimg, (0, 0))
        screen.blit(youwin, (230, 50))
        screen.blit(utime, (200, 150))
        screen.blit(stopwatchImg, (350, 250))
        screen.blit(bt1, (150, 350))
        screen.blit(bt2, (160, 400))
        pygame.draw.rect(screen, WHITE, [100, 450, 600, 100])
        screen.blit(goback, (250, 485))
        if 100<=mx<=700 and 450<=my<=550:
            pygame.draw.rect(screen, BLUE, [100, 450, 600, 100])
            screen.blit(goback, (250, 485))
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                finale=False
                menu=True
                game=False
                jump1=False
                jump2=False
        
    if instruc==True:
        screen.blit(backg, (0, 0))
        screen.blit(instructions2, (180, 60))
        screen.blit(text1, (35, 140))
        screen.blit(text2, (35, 200))
        screen.blit(text3, (60, 220))       
        screen.blit(text4, (35, 280))
        screen.blit(text5, (60, 300))
        screen.blit(text6, (35, 360))
        

        if 210<=mx<=610 and 400<=my<=500:
            pygame.draw.rect(screen, BLUE, [210, 400, 400, 100])
        else:
            pygame.draw.rect(screen, WHITE, [210, 400, 400, 100])

        screen.blit(goback, (260, 440))

    pygame.display.update()
            
pygame.quit()
