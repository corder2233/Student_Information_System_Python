from tkinter import *
import sqlite3
import os
def checklog(event):
	os.system('cls')
	con = sqlite3.connect("demo.db")
	cursor = con.cursor()
	row=cursor.execute("select * from myregdata where name=? and pass=?",(e1.get(),e2.get())).fetchall()
	if len(row)>=1:
		win.destroy()
		os.system('studwelcome.py 1')
	else:
		win.destroy()
		os.system('error.py 1')	
		
	con.commit();
	con.close()


win = Tk()
win.title("Student Login")
lb=Label(win,text="Student Login",font=('Arial',20))
lb1=Label(win,text='User Name',font=('Arial',14))
e1=Entry(win,font=('Arial',10))
lb2=Label(win,text='Password',font=('Arial',14))
e2=Entry(win,font=('Arial',10),show='*')
btn=Button(win,text="Login",font=('Arial',12))
win.geometry("400x300+150+100")
lb.place(x=130,y=30)
lb1.place(x=40,y=80)
e1.place(x=200,y=80)
lb2.place(x=40,y=110)
e2.place(x=200,y=110)
btn.place(x=210,y=140)
btn.bind('<Button>',checklog)
win.mainloop()