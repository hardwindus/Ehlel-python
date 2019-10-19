# from tkinter import *
# window=tk()


# import tkinter
# window=tkinter.Tk()
# # lable -  text, zurag gargaj haruuldag
# # Button 

# # def doClick():
# #     print("Tovch daragdlaa")


# birthYear=tkinter.StringVar()

# output=tkinter.Text(window, width=20, height=5, wrap="none",state="disabled")

# def doClick():
#     output["state"]="normal"
#     # output.insert("end","Text entered: "+birthYear.get())
#     output.insert("end", "tanii nas:"+str(2019-int(birthYear.get())))
#     output.insert("end","\n")
#     output["state"]="disabled"
   

# mylabel=tkinter.Label(window,  text="My text label")
# theImage=tkinter.PhotoImage(file="google1.png")
# # mylabel["background"]="#00FF00"
# # mylabel["foreground"]="#CC0000"
# mylabel["image"]=theImage
# mylabel["padx"]=15
# mylabel["pady"]=15
# mylabel.pack()


# entryWidget=tkinter.Entry(window, textvariable=birthYear)
# entryWidget["background"]="green"
# entryWidget.pack()

# MyButton=tkinter.Button(window, text="My button",command=doClick)
# MyButton.pack()

# output.pack()

# window.mainloop()

# from tkinter import *

# window=Tk()

# float

# def metricChanged():
#     print("OK:"+digr.get())

# digr=StringVar()

# check=Checkbutton(window, text="Temperature unit is Celsius",
#     command=metricChanged, Variable=digr,
#     onvalue="celsius", offvalue="farenheit")




# Radiobutton(window, text="Farenheit", variable=v, value="F").pack()
# Radiobutton(window, text="Celsius", variable=v, value="C").pack()
# difr.set("")

# MyButton=Button(window, text="Convert",command=doClick)
# MyButton.pack()


# window.mainloop()

# import tkinter as tk
# from tkinter import ttk
 
# app = tk.Tk() 
# app.geometry('200x100')

# labelTop = tk.Label(app,
#                     text = "Choose your favourite month")
# labelTop.grid(column=0, row=0)

# comboExample = ttk.Combobox(app, 
#                             values=[
#                                     "January", 
#                                     "February",
#                                     "March",
#                                     "April"])
# print(dict(comboExample)) 
# comboExample.grid(column=0, row=1)
# comboExample.current(1)

# print(comboExample.current(), comboExample.get())

# app.mainloop()


from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

mainloop()
