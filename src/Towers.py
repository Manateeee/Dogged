from Tower import Tower

class Towers:
    def __init__(self):
        self.tower = Tower("Utils\Pictures\Towers.png", (255, 0, 255), 50 , 50)
        self.tower.add_tower("Tower1", 20, 200, 6, 1, 200, 0, 0, "null")
        self.tower.add_tower("Tower2", 30, 500, 2, 10, 300, 50, 0, "null")

        self.tower_list = list()
        self.tower_list.append("Tower1")
        self.tower_list.append("Tower2")

        self.loaded_towers = list()

    def render(self, screen):
        for i in range(len(self.loaded_towers)):
            tower = self.tower.get_tower(self.loaded_towers[i][0])
            screen.blit(self.tower.image, (int(self.loaded_towers[i][1]),int(self.loaded_towers[i][2])), tower.rect)
               

    def new_tower(self, name, x, y):
        a = [name, x,y]
        self.loaded_towers.append(a)