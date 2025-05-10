import pygame                                   #loading pygame library
pygame.init()                                   #initializes all the modules 
pygame.display.set_caption("Space Invaders Remastered") #the window name
screen = pygame.display.set_mode((800, 800)) #set_mode has the job of creating a surface object to draw on
gameRunning = True
clock = pygame.time.Clock()                  #created a clock object
while gameRunning:
    screen.fill((0, 0, 128))                 #make the background dark blue

    for event in pygame.event.get():         #the get function comes from the event submodule and lists all the events
        if event.type == pygame.QUIT:        #event is an instance of Event class, type is an attribue of it
            gameRunning = False              #close the loop
    pygame.display.update()
    clock.tick(60)

pygame.quit()