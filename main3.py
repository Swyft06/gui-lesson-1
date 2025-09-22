from tkinter import *

root = Tk()

root.geometry("450x300")
root.title("4 buttons")

btn1 = Button(root,text = "button 1",background = "blue",fg="white",bd = 5,command = root.destroy)
btn1.pack(side = "top",pady = 5)

btn2 = Button(root,text = "button 2", background = "green",fg="white", bd = 5,command = root.destroy)
btn2.pack(side= "left",padx = 5)

btn3 = Button(root,text = "button 3", background = "red",fg="white", bd=5,command = root.destroy)
btn3.pack(side = "bottom",pady=5)

btn4 = Button(root,text = "button 4", background = "orange", fg = "white", bd=5,command = root.destroy)
btn4.pack(side = "right",padx = 5)
root.mainloop()
