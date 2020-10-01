from EnemyType import EnemyType

class Enemies:
    
    def __init__(self):
        self.Enemy = EnemyType()
        self.Enemy.add_Enemy("Peepo",0 , 5 , 0 , 0)

        #List of the EnemyTypes
        self.Enemy_list = list()
        self.Enemy_list.append("Peepo")