from tkinter import *
root = Tk()

root.title("Login screen")
root.config(background="light blue")
root.geometry("450x300")

username_label = Label(root, text="Username")
username_label.place(x=40,y=60)

username_entry = Entry(root, width = 50)
username_entry.place(x=100,y=60)

password_label = Label(root,text="Password")
password_label.place(x=40,y=100)

password_entry = Entry(root,width=50,show='*')
password_entry.place(x=100,y=100)

login_button = Button(root,text = "Login")
login_button.place(x=40,y=140,)

root.mainloop()
