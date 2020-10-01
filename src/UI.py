import pygame
class UI:
    

    pygame.init()
    screen = pygame.display.set_mode((1200,800))

    finished = False # 0 < 10 --> True / 10 < 10 --> False
    screen.fill((255,255,255))
    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        rectButtonBar = pygame.Rect(0,750,1200,50) # x,y,width,height

        color = (162,155,108) # R,G,B
        pygame.draw.rect(screen,color,rectButtonBar)
        pygame.display.flip()

    def Text(self): #Noch am arbeiten
        import pygame

        

        rectButtonBar = pygame.Rect(0,450,1200,50) # x,y,width,height
        color = (162,155,108) # R,G,B
        pygame.draw.rect(self.screen,color,rectButtonBar)

        pygame.display.update()
