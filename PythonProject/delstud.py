from tkinter import *
import sqlite3
import os

def backpage(event):
	win.destroy()
	os.system('studwelcome.py 1')
def delrec(event):
	con = sqlite3.connect("demo.db")
	cur = con.cursor()
	cur.execute("delete from studrecord where regno=?",(e.get(),))
	print('Record is deleted..')
	con.commit()
	con.close()

win = Tk()
win.title("Student Registration-Delete Record")
lb=Label(win,text="Enter Regno to Delete",font=('Arial',11))
e=Entry(win,font=('Arial',11))
btn1=Button(win,text='Delete',font=('Arial',12))
btn=Button(win,text="Back",font=('Arial',12))
win.geometry("400x300+150+100")
lb.place(x=10,y=30)
e.place(x=170,y=30)
btn1.place(x=320,y=30)
btn.place(x=210,y=240)
btn.bind('<Button>',backpage)
btn1.bind('<Button>',delrec)
win.mainloop()