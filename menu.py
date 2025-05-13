import pygame

def show_menu(screen):
    menuClock = pygame.time.Clock()
    menuFont = pygame.font.Font(None, 12) #access font module and Font function to make the font none size 12. creates a font object.

    startText = menuFont.render("Start", True, (255, 255, 255)) #render takes our font object and creates a surface object that is text
    quitText = menuFont.render("Quit", True, (255, 255, 255))

    startCenter = startText.get_rect(center=(400, 600)) #creating a rect object from our newly made surface object
    quitCenter = quitText.get_rect(center=(400, 400))

    #the menu loop
    while True:                     
        screen.fill((0, 0, 128)) #navyblue background for screen object

        #blit(source, destination)   blit(surface object, rect object), drawing a rect object on a surface object
        screen.blit(startText, startCenter)
        screen.blit(quitText, quitCenter)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if startCenter.collidepoint(event.pos):      #event.pos is part of the dictionary attributes of the event object
                    return "start"                           #these attributes are somewhat like private member variables in c++, but theyre public
                elif quitCenter.collidepoint(event.pos):     #the event.pos returns a set of coordinates that are checked against the coordinates of the rect obj
                    return "quit"

        pygame.display.flip()   #runs at the end of the loop and updates the frame of the screen, a method of the clock obj we made above
        menuClock.tick(60)