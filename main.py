import pygame                                   #loading pygame library
from menu import show_menu                      #import the show_menu function from menu.py
from player import Player                       #import the player class
from bullet import Bullet                       #import the bullet class 
from enemy import Enemy                         #import the enemy class



pygame.init()                                   #initializes all the modules 
pygame.display.set_caption("Space Invaders Remastered") #the window name
screen = pygame.display.set_mode((800, 800)) #set_mode has the job of creating a surface object to draw on
gameRunning = True
clock = pygame.time.Clock()                  #created a clock object

choice = show_menu(screen)                   #pass screen as arg for show_menu function
player1 = Player(375, 700)                   #our player is created and spawned at these coordinates

bullets = []                                 #array to track our bullets
enemies = []

#4 rows and 8 columns of enemies, adjustable spacing for enemies
rows = 4
cols = 8
vert = 60
horiz = 90

#start at y = 60 (because 60 + 60 * 0 = 60 + 0), then change the y coordinate by 60 (60, 120, 180, etc)
#for each x coordinate, start at x = 60 (because 60 + 90 * 0 = 60 + 0) 
#then change x coordinate by 90 (60, 150, 240, etc)
#create a new Enemy object using the updated coordinates 
for i in range(rows):
    y = 60 + i * vert
    for j in range(cols):
        x = 60 + j * horiz
        enemies.append(Enemy(x, y))

enemyDirection = 1 #1 is right, -1 is left

if choice == "start":                       
    gameRunning = True                      #continue game loop 
    while gameRunning:                      #game loop
        screen.fill((0, 0, 128))            #dark blue background
        for event in pygame.event.get():    #search event list
            if event.type == pygame.QUIT:   #quit event found, program exits 
                gameRunning = False         #game loop ends

            if event.type == pygame.KEYDOWN:              #type attribute of event object for pressing a key    
                if event.key == pygame.K_SPACE:           #key attribute of event object for what type of key
                    bullets.append(player1.shoot())       #shoot creates a bullet object which is added to our bullets array
        keyStates = pygame.key.get_pressed()              #creates an array called "keystates" that has booleans for every key and "True" for the ones pressed down
        
        player1.move(keyStates)                           #send the keystates array as argument to move 
        player1.draw(screen)

        for enemy in enemies:
            enemy.rect.x += enemy.horizSpeed * enemyDirection       #move enemies + or - pased on enemyDirection values (1 or -1)
            enemy.draw(screen)                                      #draw enemies each frame so you capture each movement

        for enemy in enemies:                                       
            if enemy.rect.right >= 800 or enemy.rect.left <= 0:     
                enemyDirection *= -1                                #if any enemy hits the border, reverse direction variable and 
                for enem in enemies:                                #change the y value of all enemies
                    enem.rect.y += enem.vertSpeed
                break


        








        for bullet in bullets[:]:            #slice whole list and make "bullets" copy
            bullet.move()                    #move the bullet upwards 5 pixels per frame
            bullet.draw(screen)
            if bullet.rect.bottom < 0:       #if the bottom y coordinate of the bullet rect is less than 0, delete it 
                bullets.remove(bullet)

        pygame.display.flip()               #update screen
        clock.tick(60)                      #fps update on clock object




if choice == "quit":                        #"quit" button selected
    pygame.quit()
