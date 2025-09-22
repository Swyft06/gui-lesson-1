#gui - graphical user interface

from tkinter import *

#create output window

root = Tk()

root.geometry("250x250")
root.title("First App")

btn = Button(root,text="Click here",background="blue",bd=10,command=root.destroy)
btn.pack(side="bottom",pady=5)


root.mainloop()
