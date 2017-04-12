from tkinter import *
 
window=Tk()

thecanvas = Canvas(window, width=740,height=740, highlightthickness=0)

def checkerboard(can):

    w=can.winfo_width()
    h=can.winfo_height()

    cellwidth = w/10
    cellheight=h/10
    # for row in range(10):
    #     for col in range(10):
    #         can.create_rectangle(col*cellwidth,row*cellheight,(col+1)*cellwidth,(row+1)*cellheight,fill='', width = 2, outline = 'orange')

            # if (row+col)%2==0:
            #     can.create_rectangle(col*cellwidth,row*cellheight,(col+1)*cellwidth,(row+1)*cellheight,fill='black')
            # else:
            #     can.create_rectangle(col*cellwidth,row*cellheight,(col+1)*cellwidth,(row+1)*cellheight,fill='red', width = 1)
    can.gif1 = PhotoImage(file = 'floor.gif')
    for row in range(10):
            for col in range(10):
                thecanvas.create_image(col*74,row*74, image = can.gif1, anchor = NW)

# gif2 = PhotoImage(file = 'boss.gif')
# thecanvas.create_image(2,2, image = gif2, anchor = NW)


thecanvas.grid(row=0,column=0)

window.update_idletasks()
checkerboard(thecanvas)

window.mainloop()