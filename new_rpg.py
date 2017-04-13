from tkinter import *

class GameLogic():

    def __init__(self, width = 600, height = 600, ):
        self.root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.hero = Hero()
        self.area = Area()
        self.canvas.bind("<KeyPress>", self.control)
        self.canvas.pack()
        self.canvas.focus_set()  # Select the canvas to be in focused so it actually recieves the key hittings
        self.area.tiles_and_walls(self.canvas, self.width, self.height)
        self.hero.hero_draw(self.canvas, 'down', self.hero.hero_coordinates[0] * self.width/10, self.hero.hero_coordinates[1] * self.height/10)
        self.root.mainloop()


    def position_check(self, x, y):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if self.area.map[y][x] == 0:
                return True
            else:
                return False
        else:
            return False


    def control(self, e):
        if e.keycode == 8320768:
            if self.position_check(self.hero.hero_coordinates[0] ,self.hero.hero_coordinates[1] - 1):
                self.hero.hero_coordinates[1] -= 1
                self.hero.hero_draw(self.canvas, 'up', self.hero.hero_coordinates[0] * self.width/10, self.hero.hero_coordinates[1] * self.height/10)


        elif e.keycode == 8255233:
            if self.position_check(self.hero.hero_coordinates[0] ,self.hero.hero_coordinates[1] + 1):
                self.hero.hero_coordinates[1] += 1
                self.hero.hero_draw(self.canvas, 'down', self.hero.hero_coordinates[0] * self.width/10, self.hero.hero_coordinates[1] * self.height/10)


        elif e.keycode == 8189699:
            if self.position_check(self.hero.hero_coordinates[0] + 1,self.hero.hero_coordinates[1]):
                self.hero.hero_coordinates[0] += 1
                self.hero.hero_draw(self.canvas, 'right', self.hero.hero_coordinates[0] * self.width/10, self.hero.hero_coordinates[1] * self.height/10)


        elif e.keycode == 8124162:
            if self.position_check(self.hero.hero_coordinates[0] - 1,self.hero.hero_coordinates[1]):
                self.hero.hero_coordinates[0] -= 1
                self.hero.hero_draw(self.canvas, 'left', self.hero.hero_coordinates[0] * self.width/10, self.hero.hero_coordinates[1] * self.height/10)


class Area():
    """docstring for ClassName"""
    def __init__(self):
        self.map = []
        self.floor_img = PhotoImage(file = "floor.gif")
        self.wall_img = PhotoImage(file = "wall.gif")


    def tiles_and_walls(self, canvas, width, height):

        self.map = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,1,1,1,0,0],
        [0,0,1,0,0,0,0,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
        
        for row in range(len(self.map)):
            for cell in range(len(self.map[row])):
                if self.map[cell][row] == 0:
                    canvas.create_image(row*width/10, cell*height/10, anchor=NW, image=self.floor_img)
                else:
                    canvas.create_image(row*width/10, cell*height/10, anchor=NW, image=self.wall_img)


class Hero():
    """docstring for Hero"""
    def __init__(self):
        self.hero_down = PhotoImage(file = "hero-down.gif")
        self.hero_up = PhotoImage(file = "hero-up.gif")
        self.hero_left = PhotoImage(file = "hero-left.gif")
        self.hero_right = PhotoImage(file = "hero-right.gif")
        self.hero_coordinates = [0,0]
        self.hero = None



    def hero_draw(self, canvas, turn, x, y):

        if turn == 'down':
            canvas.delete(self.hero)
            self.hero = canvas.create_image(x, y, image = self.hero_down, anchor = NW)

        elif turn == 'up':
            canvas.delete(self.hero)
            self.hero = canvas.create_image(x, y, image = self.hero_up, anchor = NW)

        elif turn == 'right':
            canvas.delete(self.hero)
            self.hero = canvas.create_image(x, y, image = self.hero_right, anchor = NW)

        elif turn == 'left':
            canvas.delete(self.hero)
            self.hero = canvas.create_image(x, y, image = self.hero_left, anchor = NW)


class Skeleton():
    def __init__(self):
        self.skeleton = PhotoImage(file = "skeleton.gif")


class Boss():
    def __init__(self):
        self.boss = PhotoImage(file = "boss.gif")











game = GameLogic()