from Enemy import Enemy
import Utils

class EnemyType:
    
    def __init__(self,image,colorkey,E_width, E_height):
        self.image = Utils.load_image(image,colorkey)
        self.E_width = E_width
        self.E_height = E_height
        self.E_types = dict()

    #Add Enemy to dict with name as key
    def add_Enemy (self, name, damage, speed,health, start_x, start_y):
        self.E_types[name] = Enemy(name,damage, speed, health, start_x,start_y, self.E_width, self.E_height )

    #Get Enemy by the name 
    def get_Enemy (self,name):
        try:
            return self.E_types[name]

        except KeyError:
            return None
