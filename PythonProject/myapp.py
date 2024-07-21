from tkinter import *
from tkinter import PhotoImage
import os
def openlogin(event):
	win.destroy()
	os.system('login.py 1')
def openmyreg(event):
	win.destroy()
	os.system('myreg.py 1')

win=Tk()
win.title('Student Info System')
lb=Label(win,text='Student Registration',font=('Arial',40))
imgpath = PhotoImage(file='C:/Users/ACER/Documents/my_project/Python_Project_college/Python Project/regimg.png')

bgimg=Label(win,image=imgpath)
bgimg.place(relheight=1, relwidth=1)
sin=Button(win,text='SignIn',font=('Arial',20),bg='white',fg='blue')
sr=Button(win, text="SignUp",font=('Arial',20),bg='white',fg='blue')
lb.place(x=50,y=40)
sin.place(x=500,y=500)
sr.place(x=1000,y=500)
sin.bind('<Button>', openlogin)
sr.bind('<Button>', openmyreg)
win.geometry("600x300+295+150")
win.mainloop()