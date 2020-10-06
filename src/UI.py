import pygame
from StatsUI import StatsUI
class UI:
    


    pygame.init()
    screen = pygame.display.set_mode((1200,800))


    finished = False # 0 < 10 --> True / 10 < 10 --> False
    
    s = StatsUI(2,10,100,1)

    while finished == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        s.DrawStats(screen)
        pygame.display.flip()


    def Text(self): #Noch am arbeiten


        
        pygame.display.update()

   


