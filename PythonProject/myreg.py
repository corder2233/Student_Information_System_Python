from tkinter import *
import sqlite3

def insdata(event):
	con = sqlite3.connect("demo.db")
	cursor = con.cursor()
	cursor.execute("insert into myregdata values (?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get()))
	print('Record is inserted')
	con.commit();
	con.close()

win=Tk()
win.title("Student Registration")
lb1=Label(win,text='Enter Name',font=('Arial',14))
e1=Entry(win,font=('Arial',12))
lb2=Label(win,text='Enter Password',font=('Arial',14))
e2=Entry(win,font=('Arial',12),show='*')
lb3=Label(win,text='Enter Email',font=('Arial',14))
e3=Entry(win,font=('Arial',12))
lb4=Label(win,text='Enter Branch',font=('Arial',14))
e4=Entry(win,font=('Arial',12))
btn=Button(win,text='Register',font=('Arial',12)) 
lb1.pack()
e1.pack()
lb2.pack()
e2.pack()
lb3.pack()
e3.pack()
lb4.pack()
e4.pack()
btn.pack()
btn.bind('<Button>',insdata)
win.geometry("400x300+200+100")
win.mainloop()
