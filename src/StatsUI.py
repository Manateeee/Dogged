import pygame

class StatsUI:
    def __init__(self, curLife , maxLife, geld, wave, uiHeight):
        self.curLife = curLife
        self.maxLife = maxLife
        self.geld = geld
        self. wave = wave
        self.uiHeight = uiHeight

    def DrawStats(self, screen):
        
        rec = pygame.Rect(0,screen.height - self.uiHeight, screen.width,self.uiHeight) # x,y,width,height
  
        color = (30,30,30) # R,G,B
        pygame.draw.rect(screen,color,rec)
        sepColor = (0,0,255)
        pygame.font.init()
        fo = pygame.font.SysFont('Comic Sans MS', 30)
        text = str(self.curLife) + '/' + str(self.maxLife)
        textsurface = fo.render(text, True, (230, 0, 0))
        curX = 5
        screen.blit(textsurface,(curX,rec.y))

        fSize = fo.size(text)
        curX = curX + rec[0] + fSize[0] + 20
        
        pygame.draw.line(screen,sepColor,(curX, rec[1]),(curX, rec.bottomleft[1]),3)

        text = str(self.geld)
        textsurface = fo.render(text, True, (230, 230, 0))

        curX = curX + 15

        screen.blit(textsurface,(curX,rec.y))

        fSize = fo.size(text)

        curX = curX + 15 + fSize[0]

        pygame.draw.line(screen,sepColor,(curX, rec[1]),(curX, rec.bottomleft[1]),3)

        text = str(self.wave)
        textsurface = fo.render(text, True, (0, 230, 0))

        curX = curX + 15

        screen.blit(textsurface,(curX,rec.y))



