from tkinter import ttk
from tkinter import *
import sqlite3
import os

def backpage(event):
	win.destroy()
	os.system('studwelcome.py 1')

win = Tk()
win.title("Student Registration-View All")
lb=Label(win,text="Student Records",font=('Arial',20))
btn=Button(win,text="Back",font=('Arial',12))
win.geometry("1100x300+180+100")
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
con1 = sqlite3.connect("demo.db")
cur1 = con1.cursor()
cur1.execute("SELECT * FROM studrecord")
rows = cur1.fetchall()    
for row in rows:
	tree.insert("", END, values=row)        
con1.close()
lb.pack()
tree.pack()
btn.pack()
btn.bind('<Button>',backpage)
win.mainloop()