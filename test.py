from tkinter import *


class GameLogic():

    def __init__(self, width, height):
        self.root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.testBoxX = 0
        self.testBoxY = 0
        # self.canvas.bind("<KeyPress>", on_key_press)
        # self.canvas.focus_set()
        self.canvas.pack()
        self.draw_tiles()
        self.root.mainloop()
        


                
    def draw_tiles(self):
        map = [
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
        self.floor_img = PhotoImage(file="floor.gif")
        self.wall_img = PhotoImage(file="wall.gif")
        for row in range(len(map)):
            for cell in range(len(map[row])):
                if map[cell][row] == 0:
                    self.canvas.create_image(row*self.width/10, cell*self.height/10, anchor=NW, image=self.floor_img)
                else:
                    self.canvas.create_image(row*self.width/10, cell*self.height/10, anchor=NW, image=self.wall_img)
        print(map,'\n')
        return map
        # self.gif2 = PhotoImage(file = 'hero-down.gif')
        # self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.gif2, anchor = NW)

    # def draw(self):
    #     self.gif2 = PhotoImage(file = 'hero-down.gif')
    #     self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.gif2, anchor = NW)



class Box(GameLogic):
    def __init__(self):
        self.testBoxX = 0 # initial coordinates
        self.testBoxY = 0



    def draw(self):
        self.gif2 = PhotoImage(file = 'hero-down.gif')
        self.canvas.create_image(self.testBoxX, self.testBoxY, image = self.gif2, anchor = NW)


    def on_key_press(self,canvas,e):
        # When the keycode is 111 (up arrow) we move the position of our box higher

        if self.e.keycode == 8320768:
            if self.testBoxY > 0:
                self.testBoxY = self.testBoxY - 74
            else:
                self.testBoxY = self.testBoxY
                
        elif e.keycode == 8255233:
            if self.testBoxY < 666:
                self.testBoxY = self.testBoxY + 74
            else:
                self.testBoxY = self.testBoxY


        elif e.keycode == 8189699:
            if self.testBoxX < 666:
                self.testBoxX = self.testBoxX + 74
            else:
                self.testBoxX = self.testBoxX


        elif e.keycode == 8124162:
            if self.testBoxX > 0:
                self.testBoxX = self.testBoxX - 74
            else:
                self.testBoxX = self.testBoxX
        # and lower if the key that was pressed the down arrow
        # draw the box again in the new position
        self.draw(canvas)
        self.bind("<KeyPress>", on_key_press)
        self.focus_set()
        self.focus_set()
        self.draw(canvas)



# Creating a box that can draw itself in a certain position
game = GameLogic(740, 740)


# # Tell the canvas that we prepared a function that can deal with the key press events
# canvas.bind("<KeyPress>", on_key_press)
# canvas.pack()

# # Select the canvas to be in focused so it actually recieves the key hittings
# canvas.focus_set()

# # Draw the box in the initial position
# box.draw(canvas)

