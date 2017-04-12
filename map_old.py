from tkinter import *

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]

root = Tk()

canvas = Canvas(root, width='800', height='800')
canvas.pack()

# image = root.Image(file='floor.gif')
# label = root.Label(image=image)
# label.pack()

# x = 10
# y = 10

# for a in range(0, 200, 10):
#     # print(a)
#     canvas.create_rectangle(x + a, y + a, x + a + 10, y + a + 10, width = 1, fill='purple')

root.mainloop()