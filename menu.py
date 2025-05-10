import pygame

def show_menu(screen):
    menuClock = pygame.time.Clock()
    menuFont = pygame.font.Font(None, 12) #access font module and Font function to make the font none size 12. creates a font object.

    startText = menuFont.render("Start", True, (255, 255, 255)) #render takes our font object and creates a surface object that is text
    quitText = menuFont.render("Quit", True, (255, 255, 255))