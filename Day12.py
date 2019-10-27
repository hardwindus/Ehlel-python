# from tkinter import *
# from tkinter import ttk

# def NewFile():
#     print("New file")

# def OpenFile():
#     print("Open file")

# def Undo():
#     print("Undo")

# window=Tk()
# menu=Menu(window)
# window.config(menu=menu)

# file_sub=Menu(menu)
# edit_sub=Menu(menu)


# menu.add_cascade(label="File", menu=file_sub)
# menu.add_cascade(label="Edit", menu=edit_sub)
# file_sub.add_command(label="New", command=NewFile)
# file_sub.add_command(label="Open",command=OpenFile)

# edit_sub.add_command(label="Undo", command=Undo)

# window.mainloop()

from tkinter import *
from tkinter import ttk

window = Tk()

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = StringVar()

topLevel = ""
topLevel_oval = ""

def drawLine():
    global canvas, window, v1, v2, v3, v4, topLevel
    canvas.create_line(int(v1.get()), int(v2.get()), int(v3.get()), int(v4.get()))
    v1.set("")
    v2.set("")
    v3.set("")
    v4.set("")
    topLevel.destroy()


def addLine():
    global window, topLevel
    topLevel = Toplevel(window)
    label1 = Label(topLevel, text="X1")
    label2 = Label(topLevel, text="Y1")
    label3 = Label(topLevel, text="X2")
    label4 = Label(topLevel, text="Y2")
    label1.grid(column=0, row=0)
    label2.grid(column=0, row=1)
    label3.grid(column=0, row=2)
    label4.grid(column=0, row=3)

    entry1 = Entry(topLevel, textvariable=v1)
    entry2 = Entry(topLevel, textvariable=v2)
    entry3 = Entry(topLevel, textvariable=v3)
    entry4 = Entry(topLevel, textvariable=v4)
    entry1.grid(column=1, row=0)
    entry2.grid(column=1, row=1)
    entry3.grid(column=1, row=2)
    entry4.grid(column=1, row=3)

    okbtn = Button(topLevel, text="OK", command=drawLine)
    okbtn.grid(column=0, row=4, columnspan=2, sticky="WE")

def drawOval():
    global canvas, window, v1, v2, v3, v5, topLevel_oval
    x1=int(v1)-int(v3)
    y1=int(v2)-int(v3)
    x2=int(v1)+int(v3)
    y2=int(v2)+int(v3)

    # x1=v1-v3
    # y1=v2-v3
    # x2=v1+v3
    # y2=v2+v3
    canvas.create_oval((x1.get(), y1.get(), x2.get(), y2.get()),fill=v5.get())
    
    # v1.set("")
    # v2.set("")
    # v3.set("")
    # v4.set("")
    # v5.set("")
    topLevel_oval.destroy()

def addOval():
    global window, topLevel_oval
    topLevel_oval = Toplevel(window)
    label1 = Label(topLevel_oval, text="X")
    label2 = Label(topLevel_oval, text="Y")
    label3 = Label(topLevel_oval, text="Radius")
    label_color = Label(topLevel_oval, text="color")
    label1.grid(column=0, row=0)
    label2.grid(column=0, row=1)
    label3.grid(column=0, row=2)
    label_color.grid(column=0, row=3)

    entry1 = Entry(topLevel_oval, textvariable=v1)
    entry2 = Entry(topLevel_oval, textvariable=v2)
    entry3 = Entry(topLevel_oval, textvariable=v3)
    entry_color = Entry(topLevel_oval, textvariable=v5)
    entry1.grid(column=1, row=0)
    entry2.grid(column=1, row=1)
    entry3.grid(column=1, row=2)
    entry_color.grid(column=1, row=3)

    okbtn = Button(topLevel_oval, text="OK", command=drawOval)
    okbtn.grid(column=0, row=4, columnspan=2, sticky="WE")

h = ttk.Scrollbar(window, orient=HORIZONTAL)
v = ttk.Scrollbar(window, orient=VERTICAL)

lineButton = Button(window, text="Line...", command=addLine)
OvalButton = Button(window, text="Oval...", command=addOval)



canvas = Canvas(window, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview


lineButton.grid(column=0, row=0)
OvalButton.grid(column=1, row=0)


ttk.Sizegrip(window).grid(column=1, row=2, sticky=(S,E))
canvas.grid(column=0, row=1, sticky=(N,W,E,S))
h.grid(column=0, row=2, sticky=(W,E))
v.grid(column=1, row=1, sticky=(N,S))
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)


# shape_id1=canvas.create_line(100,100,200,100)
# canvas.itemconfigure(shape_id1, fill='red', width=5)

# canvas.create_arc((100,100,200,200),fill="green", width=5)

# canvas.create_rectangle((50,50,100,100), fill='blue')
# canvas.create_oval((50,50,200,200), fill='blue')


# canvas.create_polygon(2,5,30,25,50,60,80,90,100,110,200,250,500,500)

# theImage=PhotoImage(file='google.jpg')
# canvas.create_image(20,100,image=theImage)

canvas.create_line((0,2,501,2), fill="black", width=2)
for x in range(0,501,10):
    canvas.create_line((x,0,x,10),fill="gray",width=1)
    
for x1 in range(0,501,50):
    canvas.create_text(x1,20 ,fill="black",font="Times 10",text=x1)
    canvas.create_line((x1,0,x1,10),fill="black",width=3)  

canvas.create_line((2,0,2,501), fill="black", width=2)
for y in range(0,501,10):
    canvas.create_line((0,y,10,y),fill="gray",width=1)

for y1 in range(0,501,50):
    canvas.create_text(20,y1 ,fill="black",font="Times 10",text=y1)
    canvas.create_line((0,y1,10,y1),fill="black",width=3)



window.mainloop()
