#Sasha Kanade & Brianna Deng
#TEJ207-3
#Mrs. Strelkovska - Period 4
#2025.05.31
#Pygame Final Project
#Final Version

import pygame
import random
import string
import time
pygame.init()
size=(800, 600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Climber - SK BD - Version 2")

#COLORS
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
BLUE=(0, 0, 255)

#FONTS
font2=pygame.font.SysFont('DroidSans', 80, False, False)
font3=pygame.font.SysFont('DroidSans', 30, False, False)
font4=pygame.font.SysFont('DroidSans', 50, False, False)

#Menu
title=font2.render("Keyboard Climbing", True, WHITE)
start=font2.render("Start", True, BLACK)
instructions1=font2.render("Instructions", True, BLACK)
instructions2=font2.render("Instructions", True, WHITE)
text1=font3.render("1. There will be a boulder with a letter above your sprite -- a monkey!", True, WHITE)
text2=font3.render("2. Your job is to press the correct lowercase letter on your keyboard", True, WHITE)
text3=font3.render("in order to move your sprite up and continue playing!", True, WHITE)
text4=font3.render("3. Remember to press the letter within 10 seconds or you will be sent", True, WHITE)
text5=font3.render("right back to the beginning!", True, WHITE)
goback=font2.render("Go Back to Menu", True, BLACK)
youwin=font2.render("YOU WIN!", True, WHITE)
utime=font2.render("Your time is:" ,True, WHITE)
bt=font3.render("Try again for a better time or challenge your friends!" ,True, WHITE)

#IMAGES
backg=pygame.image.load('bg.png')
backg=pygame.transform.scale(backg, (800,600))
boulder=pygame.image.load('boulder.png')
boulder=pygame.transform.scale(boulder, (350,230))
homeb=pygame.image.load('homeb.png')
homeb=pygame.transform.scale(homeb, (75,75))
gameover=pygame.image.load('gameover.png')
gameover=pygame.transform.scale(gameover, (800,600))
finaleimg=pygame.image.load('finale.png')
finaleimg=pygame.transform.scale(finaleimg, (800,600))

#Sprite
monks=pygame.image.load('Monkey stand.png')
monks=pygame.transform.scale(monks,(200,200))
monkj=pygame.image.load('monkey jump.png')
monkj=pygame.transform.scale(monkj,(200,200))

#Random Letters
lets=[]
lets.append("a")
for i in range(70):
    l=random.choice(string.ascii_letters)
    l=l.lower()
    lets.append(l)
letter=lets[0]

#Speeds
speedx1=0
speedy1=41

speedx2=-41
speedy2=-13.7

speedx3=41
speedy3=13.7

speedx=0
speedy=0

scroll=10
platforms=[(60, 280), (440, 75)]  
current=0 
x, y = platforms[current]
correct=False
s=0
sec=0
mins=0
score=0

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
stopwatchImg=font2.render("0:00", True, WHITE)

#Variables
counter=0
x=540
y=305
order=0
bposition=int
'''
jump_path = [(x+i*-41, y+i*-13.7) for i in range(10)] 
'''
timesec=0
timemin=0
downdown=-25

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
        letter=lets[order]
    letterImg=font2.render(letter, True, WHITE)
    
    #Counter for Time
    counter+=1
    counter=counter%1200
    
    #Boulder Position
    if counter<600:
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
                    score=0
                    mins=0
                    secs=0
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
        mins=0
        secs=0
            

    if game==True:
        screen.blit(homeb, (5, 5))
        
        jump_steps=10
        jumping=False

        if correct==True:
            score+=1
            if score==50:
                finale=True
                game=False
                
            jumping=True
            start_x, start_y=x, y
            if bposition==1:
                end_x, end_y=60, 280
            else:
                end_x, end_y=540, 75

            path=[] #Create path (Hardcode? Or use loop?-SK)
            for i in range(11):
                x2=start_x+(end_x - start_x)*i//10
                y2=start_y+(end_y-start_y)*i//10
                path.append((x2, y2))
            #Use the hardcoded path to jump to next boulder
            for pos in path:
                screen.blit(backg, (0, 0))
                screen.blit(homeb, (5, 5))

                if bposition==1: #b1
                    #screen.blit(boulder, (435, 400))
                    screen.blit(boulder, (60, 280))
                    screen.blit(letterImg, (230, 280))
                else: #b2
                    #screen.blit(boulder, (435, 400))
                    screen.blit(boulder, (440, 75))
                    screen.blit(letterImg, (610, 75))

                screen.blit(monkj, pos)  
                pygame.display.update()
                pygame.time.delay(20)

            for i in range(11):
                if bposition==1:
                    screen.blit(boulder, (60, 280-(i*downdown)))
                    screen.blit(monks, (60,280-(i*downdown)))
                    screen.blit(backg, (0, 0))
                    screen.blit(homeb, (5, 5))
                else:
                    screen.blit(boulder, (440, 75-(i*downdown)))
                    screen.blit(monks, (540,75-(i*downdown)))
                    screen.blit(backg, (0, 0))
                    screen.blit(homeb, (5, 5))

                pygame.display.update()
                pygame.time.delay(20)
            if correct==False:
                game=False
                fail=True
        #Final standing position-needs work -SK
            x, y=end_x, end_y
            screen.blit(monks, (x, y))
            if bposition==1:
                screen.blit(boulder, (440,75))
               
    
            else:
                screen.blit(boulder, (60,280))
            
            pygame.display.update()
            pygame.time.delay(100)

            correct=False
            if bposition==1:
                counter=600
                #screen.blit(boulder, (435, 400))
                screen.blit(boulder, (60, 280))
                bposition=2
            else:
                counter=0
                #screen.blit(boulder, (435, 400))
                screen.blit(boulder, (440, 75))
                bposition=1
       
        screen.blit(monks, (x, y)) 

        if bposition==1:
            screen.blit(boulder, (60, 280))
            screen.blit(letterImg, (230, 280))
        else:
            screen.blit(boulder, (440, 75))
            screen.blit(letterImg, (610, 75))

        if not correct and counter in [599, 1199]:
            print("fall")
            menu=False
            fail=True


    # Stopwatch
        s+=1
        s=s%60
        if s==0:
            sec+=1
            if sec==60:
                mins+=1
                sec=0
            if sec<10:
                stopwatchImg=font2.render(f"{mins}:0{sec}", True, WHITE)
            else:
                stopwatchImg=font2.render(f"{mins}:{sec}", True, WHITE)
        scoree=font2.render(f"{score}", True, WHITE)
        screen.blit(scoree, (600,5))
        screen.blit(stopwatchImg, (380, 5))

       
    if fail==True:
        score=0
        screen.blit(gameover, (0,0))
        pygame.draw.rect(screen, WHITE, [100,450,600,100])
        screen.blit(goback, (160,450))
        
        if 100<=mx<=700 and 450<=my<=550:
            pygame.draw.rect(screen, BLUE, [100,450,600,100])
            screen.blit(goback, (160,450))
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                fail=False
                menu=True
                game=False
                score=0
    if finale==True:
        screen.blit(finaleimg, (0,0))
        screen.blit(youwin, (230,50))
        screen.blit(utime, (230,100))
        screen.blit(stopwatchImg, (300, 175))
        screen.blit(bt, (140,250))
        pygame.draw.rect(screen, WHITE, [100,450,600,100])
        screen.blit(goback, (160,450))
        
        if 100<=mx<=700 and 450<=my<=550:
            pygame.draw.rect(screen, BLUE, [100,450,600,100])
            screen.blit(goback, (160,450))
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                finale=False
                menu=True
                game=False
                score=0
        
        
    if instruc==True:
        screen.blit(backg, (0, 0))
        screen.blit(instructions2, (180, 100))
        screen.blit(text1, (40, 200))
        screen.blit(text2, (40, 260))
        screen.blit(text3, (65, 280))       
        screen.blit(text4, (40, 340))
        screen.blit(text5, (65, 360))
        mins=0
        secs=0
        if 210<=mx<=610 and 400<=my<=500:
            pygame.draw.rect(screen, BLUE, [210, 400, 400, 100])
        else:
            pygame.draw.rect(screen, WHITE, [210, 400, 400, 100])

        screen.blit(goback, (260, 440))

    pygame.display.update()
            
pygame.quit()
