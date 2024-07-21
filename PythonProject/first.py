from tkinter import *
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
sin=Button(win,text='SignIn',font=('Arial',30))
sr=Button(win, text="SignUp",font=('Arial',30))
lb.place(x=50,y=40)
sin.place(x=60,y=100)
sr.place(x=300,y=100)
sin.bind('<Button>', openlogin)
sr.bind('<Button>', openmyreg)
win.geometry("600x300+260+100")
win.mainloop()