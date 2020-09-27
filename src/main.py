import pygame
from TileMap import TileMap

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))

    pygame.display.set_caption("dogged")

    frames = pygame.time.Clock()

    map = TileMap("Utils/Text/MapV1.txt")
    

    running = True
    while running:
        frames.tick(60)

        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein QUIT-Event finden.
            if event.type == pygame.QUIT:
                running = False
            
            # Wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird posten wir ein QUIT-Event in Pygames Event-Warteschlange.
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
           
        screen.fill((0,0,0))
        map.render(screen)
        

        pygame.display.flip()


if __name__ == '__main__':
    main()