from tkinter import *

class Game_objects:
    def __init__(self,root,canvas,background=""):
        self.root = root
        self.canvas = canvas
        self.background = background
        self.photo = PhotoImage(file=self.background)

    def create_object(self,x,y):
        self.imagine = self.canvas.create_image(x+31,y+31,image=self.photo)

class Wall(Game_objects):
    def __init__(self,root,canvas,background="wall.png"):
        super().__init__(root,canvas,background)

class Floor(Game_objects):
    def __init__(self,root,canvas,background="floor.png"):
        super().__init__(root,canvas,background)

class Hero(Game_objects):
    def __init__(self,root,canvas,background="hero-down.png"):
        super().__init__(root,canvas,background)
        self.x = 0
        self.y = 0
        self.create_object(self.x,self.y)
        self.coordinates = Map(root,canvas)

    def move(self,string):
        current_coordinates_x = self.x/72
        current_coordinates_y = self.y/72
        if self.coordinates.map()[int(current_coordinates_x)][int(current_coordinates_y)] == 1:
                self.photo = PhotoImage(file=self.background)
                if self.background == "hero-left.png":
                    self.x += 72
                elif self.background == "hero-up.png":
                    self.y += 72
                elif self.background == "hero-down.png":
                    self.y -= 72
                elif self.background == "hero-right.png":
                    self.x -= 72
        if string == "up":
            self.background = "hero-up.png"
            self.photo = PhotoImage(file=self.background)
            self.y -= 72
            if self.y < 0:
                self.y = 0
        elif string == "down":
            self.background = "hero-down.png"
            self.photo = PhotoImage(file=self.background)
            self.y += 72
            if self.y > 648:
                self.y = 648
        elif string == "left":
            self.background = "hero-left.png"
            self.photo = PhotoImage(file=self.background)
            self.x -= 72
            if self.x < 0:
                self.x = 0 
        elif string == "right":
            self.background = "hero-right.png"
            self.photo = PhotoImage(file=self.background)
            self.x += 72
            if self.x > 648:
                self.x = 648
        self.create_object(self.x,self.y)


class Map:
    def __init__(self,root,canvas):
        self.root = root
        self.canvas = canvas
        self.floor = Floor(self.root,self.canvas)
        self.wall = Wall(self.root,self.canvas)

    def map(self):
        self.game_area = [
        [0, 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0],
        [0, 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0],
        [0, 1 , 1 , 1 , 0 , 1 , 0 , 1 , 1 , 0],
        [0, 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0],
        [1, 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0],
        [0, 1 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0],
        [0, 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0],
        [0, 0 , 0 , 0 , 0 , 1 , 1 , 0 , 1 , 0],
        [0, 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 0],
        [0, 0 , 0 , 1 , 0 , 1 , 1 , 0 , 0 , 0]
        ]
        return self.game_area

    def crt_objts_map(self):
        for i in range(len(self.game_area)):
            for j in range(len(self.game_area[i])):
                if self.game_area[i][j] == 1:
                    self.wall.create_object(i*72,j*72)
                if self.game_area[i][j] == 0:
                    self.floor.create_object(i*72,j*72)
        

class Game:
    def __init__(self):
        root = Tk()
        canvas = Canvas(root, width=720, height=720, background="black")
        game = Game_objects(root,canvas)
        map_inst = Map(root,canvas)
        map_inst.map()
        map_inst.crt_objts_map()
        self.hero = Hero(root,canvas)
        canvas.bind("<KeyPress>", self.on_key_press)
        canvas.pack()
        canvas.focus_set()
        root.mainloop()

    def on_key_press(self,e):
        if e.keycode == 38:
            self.hero.move("up")
        elif e.keycode == 40:
            self.hero.move("down")
        elif e.keycode == 39:
            self.hero.move("right")
        elif e.keycode == 37:
            self.hero.move("left")
        self.hero.move("")
        
            
game = Game()