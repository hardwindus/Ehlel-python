# from tkinter import *

# window=Tk()

# frame1=Frame(window, bd=5, relief='raised')

# btn1=Button(frame1, text="Btn 1")
# btn1.pack(expand=True, fill=BOTH, side=LEFT)

# btn2=Button(frame1, text="Btn 2")
# btn2.pack(side=LEFT)

# frame1.pack(expand=True, fill=BOTH,side=TOP)

# lbl1=Label(window, text="Label 1")
# lbl1.pack(side=BOTTOM)

# window.mainloop()


# from tkinter import *
# from tkinter import messagebox

# username="Admin"
# password="123"



# window=Tk()

# usernameVar=StringVar()
# passwordVar=StringVar()


# window.geometry=("200x300")
# window.resizable(FALSE, FALSE)

# def doLogin():
#     if usernameVar.get()==username and passwordVar.get()==password:
#         print(messagebox.showinfo("Garchig","Login success!"))
#     else:
#         print(messagebox.showinfo("Garchig","Login Error!"))


# MyFrame=Frame(window, bd=5)
# SecondFrame=Frame(window,bd=5)

# lbl_name=Label(MyFrame, text="Name: ")
# lbl_name.grid(row=0, column=0,sticky=W)

# lbl_password=Label(MyFrame, text="Password: ")
# lbl_password.grid(row=1, column=0,sticky=W)

# entry_name=Entry(MyFrame, textvariable=usernameVar)
# entry_name.grid(row=0,column=1)


# entry_password=Entry(MyFrame, show='*',textvariable=passwordVar)
# entry_password.grid(row=1,column=1)

# button_login=Button(SecondFrame, text="Login", command=doLogin)
# button_login.grid(columnspan=2)

# MyFrame.pack()
# SecondFrame.pack()

# window.mainloop()


# from tkinter import *
# from tkinter import messagebox

# username="Admin"
# password="123"

# window=Tk()

# usernameVar=StringVar()
# passwordVar=StringVar()


# window.geometry=("200x300")
# window.resizable(FALSE, FALSE)

# def doLogin():
#     if usernameVar.get()==username and passwordVar.get()==password:
#         print(messagebox.showinfo("Garchig","Login success!"))
#     else:
#         print(messagebox.showinfo("Garchig","Login Error!"))


# lbl_name=Label(window, text="Name: ")
# lbl_name.grid(row=0, column=0,sticky=W)

# lbl_password=Label(window, text="Password: ")
# lbl_password.grid(row=1, column=0,sticky=W)

# entry_name=Entry(window, textvariable=usernameVar)
# entry_name.grid(row=0,column=1)

# entry_password=Entry(window, show='*',textvariable=passwordVar)
# entry_password.grid(row=1,column=1)

# button_login=Button(window, text="Login", command=doLogin, height=1, width=10)
# button_login.grid(row=2,columnspan=2)

# window.mainloop()


# from tkinter import filedialog
# from tkinter import *
# from tkinter import messagebox

# def toOpen():
#     filename = filedialog.askopenfilename()
#     messagebox.showinfo("Open file",filename)

# def toSave():
#     filename = filedialog.asksaveasfilename()
#     messagebox.showinfo("Saved file",filename)

# def toSelect():
#     dirname = filedialog.askdirectory()
#     messagebox.showinfo("Selected folder",dirname)


# window=Tk()

# button_open=Button(window, text="Open File", command=toOpen)
# button_open.pack()

# button_save=Button(window, text="Save to File", command=toSave)
# button_save.pack()

# button_select=Button(window, text="Select Folder", command=toSelect)
# button_select.pack()

# window.mainloop()


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import codecs

 
# fileobject.write("The text")
# fileobject.write("\n")
# fileobject.write("123")
# fileobject.close()


window=Tk()

textvalue="Hi"

MyfileTypes=(("text files","*.txt"),("all files","*.*"))

def toOpen():
    filename = filedialog.askopenfilename(filetypes = MyfileTypes)
    messagebox.showinfo("Open file",filename)
    if(filename!=""):
        fileobject=codecs.open(filename,"r",encoding="utf-8")
        print(fileobject.readlines())
        content=""
        lines=fileobject.readlines()
        for row in lines:
            content=content+row
        textbox.insert('2.end',content)


def toSave():
    filename = filedialog.asksaveasfilename()
    messagebox.showinfo("Saved file",filename)

def toSelect():
    dirname = filedialog.askdirectory()
    messagebox.showinfo("Selected folder",dirname)


textbox=Text(window, height=5, width=100)
# textbox.insert('1.end',"con")
textbox.pack()

button_open=Button(window, text="Open File", command=toOpen)
button_open.pack()

button_save=Button(window, text="Save to File", command=toSave)
button_save.pack()

button_select=Button(window, text="Select Folder", command=toSelect)
button_select.pack()

window.mainloop()
