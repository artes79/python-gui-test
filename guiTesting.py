from tkinter import *


root = Tk()

def myClick():
    myLabelClick = Label(root, text="Look! I clicked a Button!!")
    myLabelClick.grid(row=1, column=0)

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is secrete")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

myButton = Button(root, text="Click Me!", command=myClick) #state=DISABLED
myButton.grid(row=0, column=1)

root.mainloop()