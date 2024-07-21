from tkinter import *
import sqlite3
import os

def backpage(event):
	win.destroy()
	os.system('studwelcome.py 1')
def uprec(event):
	con1 = sqlite3.connect("demo.db")
	cur1 = con1.cursor()
	cur1.execute("update studrecord set name=?,email=? where regno=?",(e1.get(),e2.get(),e.get(),))
	print('Record is updated..')
	con1.commit()
	con1.close();

def showrec(event):
	con = sqlite3.connect("demo.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM studrecord where regno=?",(e.get(),))
	rows = cur.fetchall()    
	if len(rows)>=1:
		e1.place(x=170,y=60)
		lb1.place(x=10,y=60)
		lb2.place(x=10,y=100)
		e2.place(x=170,y=100)

		print('Record found...')
	con.close()

win = Tk()
win.title("Student Registration-Edit Record")
lb=Label(win,text="Enter Regno to Edit",font=('Arial',11))
e=Entry(win,font=('Arial',11))
btn1=Button(win,text='Show',font=('Arial',12))
btn=Button(win,text="Back",font=('Arial',12))
win.geometry("400x300+150+100")
lb.place(x=10,y=30)
e.place(x=170,y=30)
btn1.place(x=320,y=30)
btn.place(x=210,y=240)
lb1=Label(win, text='Enter new Name')
e1=Entry(win)
lb2=Label(win, text='Enter new Email')
e2=Entry(win)
b=Button(win,text='Update')
b.place(x=320,y=150)
b.bind('<Button>',uprec)
	
btn.bind('<Button>',backpage)
btn1.bind('<Button>',showrec)
win.mainloop()