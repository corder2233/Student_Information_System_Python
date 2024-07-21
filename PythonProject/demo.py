import tkinter as tk
from tkinter import ttk
import sqlite3;
def View():
    con1 = sqlite3.connect("demo.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM studrecord")
    rows = cur1.fetchall()    
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)        
    con1.close()
root = tk.Tk()
tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Name")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Regno")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Email")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Branch")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Branch")


tree.pack()
button1 = tk.Button(text="Display data", command=View)
button1.pack(pady=10)
root.mainloop()