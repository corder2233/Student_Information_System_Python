from tkinter import ttk
from tkinter import *
import sqlite3
import os

def backpage(event):
	win.destroy()
	os.system('studwelcome.py 1')

def view(event):
	tree = ttk.Treeview(win, column=("c1", "c2", "c3","c4","c5"), show='headings')
	tree.column("#1")
	tree.heading("#1", text="Name")
	tree.column("#2")
	tree.heading("#2", text="Regno")
	tree.column("#3")
	tree.heading("#3", text="Email")
	tree.column("#4")
	tree.heading("#4", text="Branch")
	tree.column("#5")
	tree.heading("#5", text="AdmissionYear")
	tree.place(x=10,y=100)
	con1 = sqlite3.connect("demo.db")
	cur1 = con1.cursor()
	cur1.execute("SELECT * FROM studrecord where regno=?",(e.get(),))
	rows = cur1.fetchall()    
	for row in rows:
		print(row)
		tree.insert("", END, values=row)        
	con1.close()
win = Tk()
win.title("Student Registration-Enquiry")
lb=Label(win,text="Enter Regno",font=('Arial',11))
e=Entry(win,font=('Arial',11))
btn1=Button(win,text='Show',font=('Arial',12))
btn=Button(win,text="Back",font=('Arial',12))
win.geometry("1100x400+150+100")
lb.place(x=10,y=30)
e.place(x=170,y=30)
btn1.place(x=320,y=30)
btn.place(x=210,y=340)
btn.bind('<Button>',backpage)
btn1.bind('<Button>',view)
win.mainloop()