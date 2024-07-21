from tkinter import *
import os
def gohome(event):
	win.destroy()
	os.system('first.py 1')

win=Tk()
win.title('Error Page')
lb=Label(win,text='Wrong Credentials! Try again',font=('Arial',20),fg='red')
btn=Button(win, text='Home', font=('Arial',15))
lb.pack()
btn.pack()
btn.bind('<Button>',gohome)
win.geometry("400x200+150+100")
win.mainloop()