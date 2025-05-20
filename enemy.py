import pygame

class Enemy:
    def __init__(self, x, y):
        self.width = 60
        self.height = 40
        self.color = (128, 128, 128)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.horizSpeed = 2
        self.vertSpeed = 5

    def move(self):
            self.rect.x += self.horizSpeed

    def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            