import pygame

class Player:                             #creating a player object 
    def __init__(self, x, y):             #constructor taking two arguments for the start location of the player (self is passed automatically when you make a player)
        self.width = 50
        self.height = 30
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(x, y, self.width, self.height)  #create a rect object at x,y location and width,height size
        self.speed = 5                                          #move five pixels per frame


        
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            print("moving left")
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            print("moving right")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)