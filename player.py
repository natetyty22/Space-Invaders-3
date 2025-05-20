import pygame
from bullet import Bullet
class Player:                             #creating a player object 
    def __init__(self, x, y):             #constructor taking two arguments for the start location of the player (self is passed automatically when you make a player)
        self.width = 50
        self.height = 30
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(x, y, self.width, self.height)  #create a rect object at x,y location and width,height size
        self.speed = 5                                          #move five pixels per frame


    #creating player movement   
    def move(self, keys):                                        #take the keys array as a parameter 
        if keys[pygame.K_LEFT] and self.rect.left > 0:           #change our x coordinate / left coordinate by our speed attribute each frame
            self.rect.x -= self.speed 
            print("moving left")
        if keys[pygame.K_RIGHT] and self.rect.right < 800:    
            self.rect.x += self.speed
            print("moving right")

    def draw(self, screen):                                       #draw our rect object
        pygame.draw.rect(screen, self.color, self.rect)
 
    def shoot(self):                                              #shooting method 
        bullet = Bullet(self.rect.centerx, self.rect.top)         #spawning bullets at center top of player     
        return bullet
        