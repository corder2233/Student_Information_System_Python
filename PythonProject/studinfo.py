from tkinter import *
from tkinter import PhotoImage
root=Tk()
root.title('My App')
root.geometry("500x400")
imgpath=PhotoImage(file='regimg.png')
bgimg=Label(root,image=imgpath)
bgimg.place(relheight=1, relwidth=1)
text=Label(root,text="Welcome to MyApp")
text.pack()
root.mainloop()