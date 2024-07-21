import os
import datetime
import tkinter as tk
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
root = tk.Tk()

def stwel(event):
	root.destroy()
	os.system('studwelcome.py 1')

cdate = datetime.datetime.now()
dt='Today '+str(cdate.day)+'-'+str(cdate.month)+'-'+str(cdate.year)

root.title('Student Registration-Report')
lb=tk.Label(root,text='Year Wise Percentage Students',font=('Arial',20))
lb.pack()
ldt=tk.Label(root,text=dt,font=('Arial',15))
ldt.pack()
frameChartsLT = tk.Frame(root)
frameChartsLT.pack()

con1 = sqlite3.connect("demo.db")
cur1 = con1.cursor()
cur1.execute("select ayear,count(*) from studrecord group by ayear")
rows = cur1.fetchall()  
yr=[]
stud=[]
for i in rows:
	yr.append(i[0]) 
	stud.append(i[1]) 

fig = Figure() # create a figure object
ax = fig.add_subplot(111) # add an Axes to the figure

ax.pie(stud, radius=1, labels=yr,autopct='%0.2f%%', shadow=True,)

chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
chart1.get_tk_widget().pack()
b=tk.Button(root,text='Back',font=('Arial',15))
b.pack()
b.bind('<Button>',stwel)
root.mainloop()