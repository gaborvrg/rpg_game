from tkinter import *

class GameLogic():

    def __init__(self, width = 720, height = 720):
        self.root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.direction = 'down'
        self.hero_down = PhotoImage(file = "hero-down.gif")
        self.hero_up = PhotoImage(file = "hero-up.gif")
        self.hero_left = PhotoImage(file = "hero-left.gif")
        self.hero_right = PhotoImage(file = "hero-right.gif")
        self.floor_img = PhotoImage(file = "floor.gif")
        self.wall_img = PhotoImage(file = "wall.gif")
        self.hero = None
        self.testBoxX = 0 # initial coordinates
        self.testBoxY = 0
        self.map()
        self.canvas.bind("<KeyPress>", self.controll)
        self.canvas.pack()
        self.canvas.focus_set()  # Select the canvas to be in focused so it actually recieves the key hittings
        self.hero_draw(self.direction)

        self.root.mainloop()


    def map(self):

        map = [
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
        
        for row in range(len(map)):
            for cell in range(len(map[row])):
                if map[cell][row] == 0:
                    self.canvas.create_image(row*self.width/10, cell*self.height/10, anchor=NW, image=self.floor_img)
                else:
                    self.canvas.create_image(row*self.width/10, cell*self.height/10, anchor=NW, image=self.wall_img)

    def hero_draw(self, turn):

        if turn == 'down':
            self.canvas.delete(self.hero)
            self.hero = self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.hero_down, anchor = NW)

        elif turn == 'up':
            self.canvas.delete(self.hero)
            self.hero = self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.hero_up, anchor = NW)

        elif turn == 'right':
            self.canvas.delete(self.hero)
            self.hero = self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.hero_right, anchor = NW)

        elif turn == 'left':
            self.canvas.delete(self.hero)
            self.hero = self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.hero_left, anchor = NW)




    def controll(self, e):

        if e.keycode == 8320768:
            if self.testBoxY > 0:
                self.testBoxY = self.testBoxY - self.height/10
                self.direction = 'up'
            else:
                self.testBoxY = self.testBoxY
                
        elif e.keycode == 8255233:
            if self.testBoxY < self.height - self.height/10:
                self.testBoxY = self.testBoxY + self.height/10
                self.direction = 'down'
            else:
                self.testBoxY = self.testBoxY

        elif e.keycode == 8189699:
            if self.testBoxX < self.width - self.width/10:
                self.testBoxX = self.testBoxX + self.width/10
                self.direction = 'right'
            else:
                self.testBoxX = self.testBoxX

        elif e.keycode == 8124162:
            if self.testBoxX > 0:
                self.testBoxX = self.testBoxX - self.width/10
                self.direction = 'left'
            else:
                self.testBoxX = self.testBoxX
        
        self.hero_draw(self.direction) # draw the box again in the new position




game = GameLogic()