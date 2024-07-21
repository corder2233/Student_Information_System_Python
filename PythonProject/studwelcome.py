from tkinter import *
import os

def logoutapp(event):
    win.destroy()
    os.system('first.py 1')

def addnew(event):
    win.destroy()
    os.system('addrecord.py 1')

def viewall(event):
    win.destroy()
    os.system('viewall.py 1')

def enquiry(event):
    win.destroy()
    os.system('enqstud.py 1')

def edit(event):
    win.destroy()
    os.system('editstud.py 1')

def delst(event):
    win.destroy()
    os.system('delstud.py 1')

def repyr(event):
    win.destroy()
    os.system('reportyear.py 1')

def repbr(event):
    win.destroy()
    os.system('reportbranch.py 1')

win = Tk()
win.title('Student Info System')
lb = Label(win, text='Student Welcome', font=('Arial', 30))
b1 = Button(win, text='Add New Student', font=('Arial', 20))
b2 = Button(win, text='View All Students', font=('Arial', 20))
b3 = Button(win, text='Enquiry Students', font=('Arial', 20))
b4 = Button(win, text='Edit Student Details', font=('Arial', 20))
b5 = Button(win, text='Delete Student Details', font=('Arial', 20))
b6 = Button(win, text='Report Year', font=('Arial', 20))
b7 = Button(win, text='Report Branch', font=('Arial', 20))
b8 = Button(win, text='Logout', bg='red', font=('Arial', 20))
lb.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b1.bind('<Button>', addnew)
b2.bind('<Button>', viewall)
b3.bind('<Button>', enquiry)
b4.bind('<Button>', edit)
b5.bind('<Button>', delst)
b6.bind('<Button>', repyr)
b7.bind('<Button>', repbr)
b8.bind('<Button>', logoutapp)

win.geometry("500x500+150+100")
win.mainloop()
