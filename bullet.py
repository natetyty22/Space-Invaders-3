import pygame

class Bullet:                                                           #created a bullet object with spawn location x, y
    def __init__(self, x, y):
        self.width = 5
        self.height = 10
        self.color = (255, 255, 255)                                    #white 
        self.rect = pygame.Rect(x, y, self.width, self.height)          #spawn coordinates and dimensions
        self.speed = 10

    def move(self):                                                     #moves UPWARD even though were subtracting because of the way pygame coordinates work 
        self.rect.y -= self.speed

    def draw(self, screen):                                             #drawing our rect object, the bullet 
        pygame.draw.rect(screen, self.color, self.rect)