import pygame                                   #loading pygame library
from menu import show_menu                      #import the show_menu function from menu.py

pygame.init()                                   #initializes all the modules 
pygame.display.set_caption("Space Invaders Remastered") #the window name
screen = pygame.display.set_mode((800, 800)) #set_mode has the job of creating a surface object to draw on
gameRunning = True
clock = pygame.time.Clock()                  #created a clock object

choice = show_menu(screen)                   #pass screen as arg for show_menu function


if choice == "start":                       
    gameRunning = True                      #continue game loop 
    while gameRunning:                      #game loop
        screen.fill((0, 0, 128))            #dark blue background
        for event in pygame.event.get():    #search event list
            if event.type == pygame.QUIT:   #quit event found, program exits 
                gameRunning = False         #game loop ends
        
        pygame.display.flip()               #update screen
        clock.tick(60)                      #fps update on clock object

if choice == "quit":                        #"quit" button selected
    pygame.quit()
