from EnemyType import EnemyType


class Enemies:
    
    def __init__(self):
        self.Enemy = EnemyType("Utils\Pictures\Peepo.png",(255,0,255),50,50)
        self.Enemy.add_Enemy("Peepo",0 , 5 , 100 , 0, 0)

        #List of the EnemyTypes
        self.Enemy_list = list()
        self.Enemy_list.append("Peepo")

        #List of Waves
        self.Waves = list()

    def render(self,screen):
        wow = self.Enemy.get_Enemy(self.Enemy_list[0])
        screen.blit(self.Enemy.image,(0,0), wow.rectangle)
