#Sasha Kanade & Brianna Deng
#TEJ207-3
#Mrs.Strelkovska-Period 4
#2025.05.28
#Pygame Final Project
#Draft 1
import pygame
import random
import string
pygame.init()
size=(800,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Climber-SK BD-Version 1")

#COLORS
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)

#Font
font=pygame.font.SysFont('DroidSans',100,True, False)
font2=pygame.font.SysFont('DroidSans', 80, False, False)
font3=pygame.font.SysFont('DroidSans',25,False,False)
#Menu
text1=font.render("Keyboard Climbing", True, WHITE)
text2=font2.render("Start", True, BLACK)
text3=font2.render("Instructions", True, BLACK)
text4=font.render("Instructions", True, WHITE)
text5=font3.render("There will be a boulder with a letter above your sprite--a monkey!", True, WHITE)
text6=font3.render("Your job is to click the correct letter on your keyboard in order to move up and continue playing!", True, WHITE)
text7=font3.render("Remember to click the letter within 10 seconds or you will be sent right back to the beggining!",True, WHITE)
text8=font2.render("Menu", True, BLACK)
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

#Clock

#Random letters
lets=[]
for i in range(70):
    b=random.choice(string.ascii_letters)
    b=b
    lets.append(b)

#Left or Right
pos=[]
for i in range(70):
    c= random.randint(1,2)
    pos.append(c)

menu=True
game=False
Intruc=False

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            mx, my =pygame.mouse.get_pos()

            if menu==True:
                if 150<=mx<=650 and 200<=my<=300:
                    menu=False
                    game=True
                elif 150<=mx<=650 and 400<=my<=500:
                    menu=False
                    Intruc=True

            elif Intruc==True:
                if 210<=mx<=610 and 400<=my<=500:
                    Intruc=False
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

    if game==True:
        screen.blit(backg, (0, 0))
        
        #Mouse Position
        pos=pygame.mouse.get_pos()
        x1=pos[0]
        y2=pos[1]
        screen.blit(backg, (0, 0))
        
        textImg=font3.render(f"x = {x1}, y = {y2}", True, WHITE)
        screen.blit(textImg, [x1+15, y2-5])

        #Letter
        letter=lets[random.randint(0, 69)]
        letterImg=font3.render(letter, True, WHITE)
        
        #Counter
        '''
        counter+=1
        counter=counter%240
        if counter==0:
        '''    
        #Monkey Animations
        direction=random.randint(1, 2)
        if direction==1:
            while t!=0:
                screen.blit(boulder, (440, 75))
                screen.blit(letterImg, (620, 105))
                t+=1
                t=t%240





    if Intruc==True:
        screen.blit(backg, (0, 0))
        screen.blit(text4, (200, 100))
        screen.blit(text5, (10, 200))
        screen.blit(text6, (10, 260))
        screen.blit(text7, (10, 320))

        if 210<=mx<=610 and 400<=my<=500:
            pygame.draw.rect(screen, BLUE, [210, 400, 400, 100])
        else:
            pygame.draw.rect(screen, WHITE, [210, 400, 400, 100])

        screen.blit(text8, (330, 420))

    pygame.display.update()

            
pygame.quit()

