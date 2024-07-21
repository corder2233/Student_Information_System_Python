from tkinter import *
import sqlite3
import os
def saverecord(event):
	con = sqlite3.connect("demo.db")
	cursor = con.cursor()
	cursor.execute("insert into studrecord values (?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
	print('Student Record is Saved...')
	con.commit();
	con.close()
	win.destroy()
	os.system('studwelcome.py 1');
       

win=Tk()
win.title("Student Registration-Add New")
lb1=Label(win,text='Enter Name',font=('Arial',14))
e1=Entry(win,font=('Arial',12))
lb2=Label(win,text='Enter Regno',font=('Arial',14))
e2=Entry(win,font=('Arial',12))
lb3=Label(win,text='Enter Email',font=('Arial',14))
e3=Entry(win,font=('Arial',12))
lb4=Label(win,text='Enter Branch',font=('Arial',14))
e4=Entry(win,font=('Arial',12))
lb5=Label(win,text='Enter Addmission year',font=('Arial',14))
e5=Entry(win,font=('Arial',12))

btn=Button(win,text='Register',font=('Arial',12)) 
lb1.pack()
e1.pack()
lb2.pack()
e2.pack()
lb3.pack()
e3.pack()
lb4.pack()
e4.pack()
lb5.pack()
e5.pack()
btn.pack()
btn.bind('<Button>',saverecord)
win.geometry("400x300+200+100")
win.mainloop()