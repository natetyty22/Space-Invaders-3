import pygame                                   #loading pygame library
from menu import show_menu                      #import the show_menu function from menu.py
from player import Player                       #import the player class
from bullet import Bullet                       #import the bullet class 
pygame.init()                                   #initializes all the modules 
pygame.display.set_caption("Space Invaders Remastered") #the window name
screen = pygame.display.set_mode((800, 800)) #set_mode has the job of creating a surface object to draw on
gameRunning = True
clock = pygame.time.Clock()                  #created a clock object

choice = show_menu(screen)                   #pass screen as arg for show_menu function
player1 = Player(375, 700)                   #our player is created and spawned at these coordinates

bullets = []                                 #array to track our bullets

if choice == "start":                       
    gameRunning = True                      #continue game loop 
    while gameRunning:                      #game loop
        screen.fill((0, 0, 128))            #dark blue background
        for event in pygame.event.get():    #search event list
            if event.type == pygame.QUIT:   #quit event found, program exits 
                gameRunning = False         #game loop ends

            if event.type == pygame.KEYDOWN:              #type attribute of event object for pressing a key    
                if event.key == pygame.K_SPACE:           #key attribute of event object for what type of key
                    bullets.append(player1.shoot())
        keyStates = pygame.key.get_pressed()              #creates an array called "keystates" that has booleans for every key and "True" for the ones pressed down
        
        player1.move(keyStates)
        player1.draw(screen)

        for bullet in bullets[:]:            #slice whole list and make "bullets" copy
            bullet.move()                    #move the bullet upwards 5 pixels per frame
            if bullet.rect.bottom < 0:       #if the bottom y coordinate of the bullet rect is less than 0, delete it 
                bullets.remove(bullet)

        pygame.display.flip()               #update screen
        clock.tick(60)                      #fps update on clock object

if choice == "quit":                        #"quit" button selected
    pygame.quit()
